import subprocess
from typing import Optional

class LlamaCppModel:
    def __init__(self, model_path: str, llama_cpp_path: str = "llama.cpp/main"):
        """
        model_path: Path to the quantized GGUF model file
        llama_cpp_path: Path to the llama.cpp executable (default assumes built in llama.cpp/main)
        """
        self.model_path = model_path
        self.llama_cpp_path = llama_cpp_path

    def generate(self, prompt: str, max_tokens: int = 128, temperature: float = 0.7) -> Optional[str]:
        """
        Run the model on the given prompt and return the generated response.
        """
        try:
            cmd = [
                self.llama_cpp_path,
                "-m", self.model_path,
                "-p", prompt,
                "-n", str(max_tokens),
                "--temp", str(temperature)
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                print(f"[ERROR] llama.cpp failed: {result.stderr}")
                return None
        except Exception as e:
            print(f"[EXCEPTION] llama.cpp call failed: {e}")
            return None 