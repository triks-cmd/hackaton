from datetime import datetime

class Work:
    def __init__(self, topic, difficulty, grade, assigned_date, due_date, submission_date):
        self.topic = topic
        self.difficulty = difficulty.lower()
        self.grade = float(grade)
        self.assigned_date = datetime.strptime(assigned_date, '%Y-%m-%d') if assigned_date else None
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d') if due_date else None
        self.submission_date = datetime.strptime(submission_date, '%Y-%m-%d') if submission_date else None

    def is_late(self):
        if self.submission_date and self.due_date:
            return self.submission_date > self.due_date
        return False

class Student:
    def __init__(self, name, expected_level, attendance):
        self.name = name
        self.expected_level = float(expected_level) if expected_level else 0.0
        self.attendance = float(attendance) if attendance else 0.0
        self.works = []

    def add_work(self, work):
        self.works.append(work)

    def calculate_final_level(self):
        if not self.works:
            return 0.0
        
        total = 0.0
        for work in self.works:
            multiplier = {
                "высокий": 1.2,
                "средний": 1.0,
                "низкий": 0.8
            }.get(work.difficulty, 1.0)
            total += work.grade * multiplier
        
        return round(total / len(self.works), 2)

def analyze_student(student):
    final_level = student.calculate_final_level()
    expected = student.expected_level
    attendance = student.attendance

    report = [
        "=== Анализ успеваемости ===",
        f"Студент: {student.name}",
        f"Ожидаемый уровень: {expected}",
        f"Фактический уровень: {final_level}",
        f"Посещаемость: {attendance}%",
        "\n=== Рекомендации ==="
    ]

    performance_ratio = final_level / expected if expected != 0 else 1
    
    if performance_ratio >= 1.1:
        report.append("✅ Отличные результаты! Превышение ожиданий.")
        report.append("Рекомендации:")
        report.append("- Выдать продвинутые задания")
        report.append("- Привлечь к менторской деятельности")
    elif performance_ratio >= 1:
        report.append("⚠️ Хорошие результаты. Соответствует ожиданиям.")
        report.append("Рекомендации:")
        report.append("- Поддерживающие задания")
        report.append("- Регулярные проверки прогресса")
    else:
        report.append("❌ Низкая успеваемость! Требуется вмешательство.")
        report.append("Срочные меры:")
        report.append("- Дополнительные занятия")
        report.append("- Индивидуальный план обучения")
        if attendance < 70:
            report.append("- Беседа по поводу посещаемости")

    return "\n".join(report)