from flask_restful import Resource
from app.models import Student, Work
from app import db

class StudentResource(Resource):
    def get(self, student_id):
        student = Student.query.get_or_404(student_id)
        return {
            'id': student.id,
            'name': student.name,
            'email': student.email,
            'performance': student.calculate_final_level()
        }

class WorkListResource(Resource):
    def get(self):
        works = Work.query.all()
        return [{
            'id': work.id,
            'topic': work.topic,
            'grade': work.grade,
            'student': work.student.name
        } for work in works]