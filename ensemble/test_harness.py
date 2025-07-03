import sys
import os
from pathlib import Path
import yaml

from ensemble.base_model import LlamaCppModel
from ensemble.ensemble import LLMEnsemble

# Load config from config.yaml if available
CONFIG_PATH = Path(__file__).parent.parent / "config.yaml"
def load_config():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, 'r') as f:
            config = yaml.safe_load(f)
        llama_cpp_path = config.get('llama_cpp_path', 'llama.cpp/build/bin/main')
        model_paths = config.get('models', [])
        return llama_cpp_path, model_paths
    else:
        print("[WARN] config.yaml not found, using default paths.")
        return "llama.cpp/build/bin/main", [
            "models/mistral.gguf",
            "models/phi2.gguf",
            "models/tinyllama.gguf",
            "models/qwen.gguf"
        ]

LLAMA_CPP_PATH, MODEL_PATHS = load_config()
models = [LlamaCppModel(model_path=mp, llama_cpp_path=LLAMA_CPP_PATH) for mp in MODEL_PATHS if os.path.exists(mp)]
ensemble = LLMEnsemble(models)

def run_prompt(prompt):
    print(f"\nPrompt: {prompt}\n")
    print("Individual model responses:")
    for i, model in enumerate(models):
        response = model.generate(prompt)
        print(f"Model {i+1}: {response}")
    print("\nEnsemble answer:")
    ensemble_response = ensemble.generate(prompt)
    print(ensemble_response)

def main():
    if len(sys.argv) > 1 and sys.argv[1].endswith('.txt'):
        # Batch mode: read prompts from file
        with open(sys.argv[1], 'r') as f:
            prompts = [line.strip() for line in f if line.strip()]
        for prompt in prompts:
            run_prompt(prompt)
    else:
        # Interactive CLI mode
        print("Eidolon Ensemble CLI. Type 'exit' to quit.")
        while True:
            prompt = input("\nEnter your prompt: ")
            if prompt.lower() in ("exit", "quit"): break
            run_prompt(prompt)

if __name__ == "__main__":
    main() 