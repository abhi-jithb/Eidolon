from typing import List, Optional
from collections import Counter
from .base_model import LlamaCppModel

class LLMEnsemble:
    def __init__(self, models: List[LlamaCppModel]):
        self.models = models

    def generate(self, prompt: str, max_tokens: int = 128, temperature: float = 0.7) -> Optional[str]:
        responses = []
        for model in self.models:
            response = model.generate(prompt, max_tokens=max_tokens, temperature=temperature)
            if response:
                responses.append(response)
        if not responses:
            print("[ERROR] No model returned a response.")
            return None
        # Majority voting
        count = Counter(responses)
        most_common = count.most_common(1)
        if most_common and most_common[0][1] > 1:
            return most_common[0][0]
        # If all responses are unique, return the first non-empty
        return responses[0] 