from flask import Blueprint, request, jsonify
from app.ai.helper import AIHelper
from app.models import Student  # или используйте свою модель студента

ai_bp = Blueprint('ai_bp', __name__, url_prefix='/ai')

@ai_bp.route('/recommendations', methods=['GET'])
def get_recommendations():
    # Для демонстрации предполагается, что ID студента передаётся как query-параметр
    student_id = request.args.get('student_id')
    if not student_id:
        return jsonify({"error": "Необходимо указать student_id"}), 400
    
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": "Студент не найден"}), 404
    
    ai_helper = AIHelper()
    recommendations = ai_helper.recommend_resources(student)
    return jsonify(recommendations)
