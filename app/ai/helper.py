class AIHelper:
    def __init__(self):
        self.knowledge_base = {
            "python": "Python — это мощный и популярный язык программирования.",
            "flask": "Flask — это легковесный веб-фреймворк для Python.",
            "machine learning": "Машинное обучение — это метод анализа данных, который автоматизирует построение моделей."
        }
        self.grader = AutoGrader()

    def detect_ai_code(self, code):
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

    def recommend_resources(self, student):
        """
        Анализирует работы студента и возвращает рекомендации:
         - список литературы/источников для подтяжки тем, по которым оценки ниже порогового значения
         - общие советы по улучшению успеваемости
        """
        weak_topics = []
        for work in student.works:
            # Если оценка ниже 6, считаем тему слабой (порог можно изменить)
            if work.grade < 6:
                weak_topics.append(work.topic.lower())
        weak_topics = set(weak_topics)
        
        # Пример базы литературы для рекомендаций по ключевым темам
        literature_db = {
            'python': [
                '«Automate the Boring Stuff with Python» - Al Sweigart',
                '«Learning Python» - Mark Lutz'
            ],
            'flask': [
                '«Flask Web Development» - Miguel Grinberg'
            ],
            'machine learning': [
                '«Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow» - Aurélien Géron'
            ],
            # можно добавить дополнительные темы и источники
        }
        
        resources = {}
        for topic in weak_topics:
            for key in literature_db:
                if key in topic:
                    resources.setdefault(key, []).extend(literature_db[key])
        
        # Если по слабым темам не найдено соответствий, можно дать общий совет
        advice = "Рекомендуется проанализировать ошибки, повторить теоретический материал и выполнять дополнительные практические задания."
        
        return {
            "resources": resources if resources else "Нет обнаруженных слабых тем на основе текущих данных.",
            "advice": advice
        }
