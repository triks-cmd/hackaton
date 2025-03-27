from datetime import datetime

class Work:
    def __init__(self, topic, difficulty, grade, assigned_date, due_date, submission_date):
        self.topic = topic
        self.difficulty = difficulty.lower()
        self.grade = grade
        self.assigned_date = assigned_date
        self.due_date = due_date
        self.submission_date = submission_date

    def is_late(self):
        return self.submission_date > self.due_date

class Student:
    def __init__(self, name, expected_level, attendance):
        self.name = name
        self.expected_level = expected_level
        self.attendance = attendance
        self.works = []

    def add_work(self, work):
        self.works.append(work)

    def calculate_final_level(self):
        if not self.works:
            return 0
        
        total = 0
        for work in self.works:
            if work.difficulty == "высокий":
                total += work.grade * 1.2
            elif work.difficulty == "средний":
                total += work.grade
            else:
                total += work.grade * 0.8
        
        return total / len(self.works)

def analyze_student(student):
    final_level = student.calculate_final_level()
    
    feedback = (
        f"Студент: {student.name}\n"
        f"Итоговый уровень: {final_level:.1f}\n"
        f"Посещаемость: {student.attendance}%"
    )
    
    characteristic = (
        f"Анализ для преподавателя:\n"
        f"Ожидаемый уровень: {student.expected_level}\n"
        f"Средний балл работ: {final_level:.1f}"
    )
    
    return feedback, characteristic