from base_model import LlamaCppModel
from ensemble import LLMEnsemble

# Replace these with actual paths to your quantized GGUF models and llama.cpp executable
MODEL_PATHS = [
    "models/model1.gguf",
    "models/model2.gguf"
]
LLAMA_CPP_PATH = "llama.cpp/main"  # Adjust if llama.cpp is elsewhere

# Instantiate models
models = [LlamaCppModel(model_path=mp, llama_cpp_path=LLAMA_CPP_PATH) for mp in MODEL_PATHS]

# Create ensemble
ensemble = LLMEnsemble(models)

# Sample prompt
def main():
    prompt = "What is the capital of France?"
    print(f"Prompt: {prompt}\n")
    print("Individual model responses:")
    for i, model in enumerate(models):
        response = model.generate(prompt)
        print(f"Model {i+1}: {response}")
    print("\nEnsemble answer:")
    ensemble_response = ensemble.generate(prompt)
    print(ensemble_response)

if __name__ == "__main__":
    main() 