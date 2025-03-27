from difflib import SequenceMatcher
import re

class AutoGrader:
    def __init__(self):
        self.rubrics = {
            "essay": {
                "criteria": ["тезис", "примеры", "структура", "аргументация"],
                "keywords": {
                    "тезис": ["главная идея", "основное положение", "центральная мысль"],
                    "примеры": ["например", "в качестве примера", "иллюстрацией"],
                    "структура": ["введение", "заключение", "первый пункт", "во-вторых"],
                    "аргументация": ["потому что", "следовательно", "таким образом"]
                }
            }
        }

    def grade_essay(self, text, topic):
        feedback = []
        score = 0
        
        for criterion in self.rubrics["essay"]["criteria"]:
            matches = sum(1 for kw in self.rubrics["essay"]["keywords"][criterion] 
                      if kw in text.lower())
            if matches < 2:
                feedback.append(f"❌ Недостаточно {criterion}")
                score -= 1
            else:
                score += 1
                feedback.append(f"✅ Хороший уровень {criterion}")
        
        if len(re.findall(r"\n\d+\.|\n•|\n\*", text)) < 3:
            feedback.append("⚠️ Слабая структура")
        
        return {
            "score": max(0, score),
            "feedback": feedback,
            "topic": topic
        }