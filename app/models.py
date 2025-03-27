from app import db
from datetime import datetime

class Student(db.Model):
    __tablename__ = 'student'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    expected_level = db.Column(db.Float)
    attendance = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Настройка отношений с каскадным удалением
    works = db.relationship(
        'Work', 
        backref='student', 
        lazy=True, 
        cascade='all, delete-orphan'
    )

    def calculate_final_level(self):
        if not self.works:
            return 0
        
        total = sum(
            work.grade * {
                "низкий": 0.8,
                "средний": 1.0,
                "высокий": 1.2
            }.get(work.difficulty.lower(), 1.0)
            for work in self.works
        )
        return round(total / len(self.works), 2)

class Work(db.Model):
    __tablename__ = 'work'
    
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(200), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    grade = db.Column(db.Float, nullable=False)
    assigned_date = db.Column(db.DateTime)
    due_date = db.Column(db.DateTime)
    submission_date = db.Column(db.DateTime)
    
    # Внешний ключ с явным именованием
    student_id = db.Column(
        db.Integer, 
        db.ForeignKey('student.id', ondelete='CASCADE'), 
        nullable=False
    )

    def is_late(self):
        return self.submission_date > self.due_date