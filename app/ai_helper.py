import random
import difflib
from .grading import AutoGrader

class AIHelper:
    def __init__(self):
        self.knowledge_base = {
            "python": "Python — это мощный и популярный язык программирования.",
            "flask": "Flask — это легковесный веб-фреймворк для Python.",
            "machine learning": "Машинное обучение — это метод анализа данных, который автоматизирует построение моделей."
        }
        self.grader = AutoGrader()

    def detect_ai_code(self, code):
        # Простой детектор по паттернам (для примера)
        ai_patterns = ["auto-generated", "TODO:", "pass  #", "..."]

        score = sum(1 for pattern in ai_patterns if pattern in code)
        probability = min(score / len(ai_patterns) * 100, 100)
        
        return {
            "ai_probability": round(probability, 2),
            "is_ai": probability > 50
        }

    def instant_answer(self, question):
        question = question.lower()
        for key in self.knowledge_base:
            if key in question:
                return self.knowledge_base[key]
        return "Я пока не знаю ответа, но могу помочь разобраться!"