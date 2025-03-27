from transformers import AutoTokenizer, AutoModel
import torch
import re
from sklearn.ensemble import RandomForestClassifier
import numpy as np

class CodeAnalyzer:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
        self.model = AutoModel.from_pretrained("microsoft/codebert-base")
        self.classifier = RandomForestClassifier()
        
        # Инициализация простой модели (для примера)
        self.classifier.fit(np.random.rand(10, 768), np.random.randint(0, 2, 10))

    def analyze_code(self, code):
        try:
            inputs = self.tokenizer(code, return_tensors="pt", truncation=True, max_length=512)
            with torch.no_grad():
                outputs = self.model(**inputs)
            embeddings = outputs.last_hidden_state.mean(dim=1).numpy()
            
            prediction = self.classifier.predict_proba(embeddings)
            return {
                "ai_prob": round(prediction[0][1] * 100, 2),
                "features": {
                    "length": len(code),
                    "comments": len(re.findall(r'#.*', code))
                }
            }
        except Exception as e:
            return {"error": str(e)}

class AIDetectorAPI:
    def __init__(self):
        self.analyzer = CodeAnalyzer()
    
    def analyze(self, code):
        return self.analyzer.analyze_code(code)