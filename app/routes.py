from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
import os
import glob
from .analysis import Student, Work, analyze_student

main_bp = Blueprint('main_bp', __name__)
REPORTS_DIR = 'reports'

def save_report(data):
    """Сохраняет полный отчет в файл"""
    os.makedirs(REPORTS_DIR, exist_ok=True)
    filename = f"{REPORTS_DIR}/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    # Создаем объекты для анализа
    student = Student(
        name=data['name'],
        expected_level=data['expected_level'],
        attendance=data['attendance']
    )
    
    work = Work(
        topic=data['topic'],
        difficulty=data['difficulty'],
        grade=float(data['grade']) if data['grade'] else 0.0,
        assigned_date=data['assigned_date'],
        due_date=data['due_date'],
        submission_date=data['submission_date']
    )
    student.add_work(work)
    
    # Генерируем анализ
    analysis = analyze_student(student)
    
    # Сохраняем в файл
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=== ДАННЫЕ СТУДЕНТА ===\n")
        f.write(f"Имя: {data['name']}\n")
        f.write(f"Ожидаемый уровень: {data['expected_level']}\n")
        f.write(f"Посещаемость: {data['attendance']}%\n\n")
        
        f.write("=== ДАННЫЕ РАБОТЫ ===\n")
        f.write(f"Тема: {data['topic']}\n")
        f.write(f"Сложность: {data['difficulty']}\n")
        f.write(f"Оценка: {data['grade']}\n")
        f.write(f"Дата выдачи: {data['assigned_date']}\n")
        f.write(f"Срок сдачи: {data['due_date']}\n")
        f.write(f"Дата сдачи: {data['submission_date']}\n\n")
        
        f.write(analysis)
    
    return filename

def get_all_reports():
    """Возвращает все сохраненные отчеты"""
    reports = []
    for filepath in glob.glob(f"{REPORTS_DIR}/*.txt"):
        filename = os.path.basename(filepath)
        try:
            # Парсим дату из имени файла
            parts = filename.split('_')
            date_part = parts[1]  # Год-месяц-день
            time_part = parts[2].split('.')[0]  # Часы-минуты-секунды
            datetime_str = f"{date_part}{time_part}"
            date = datetime.strptime(datetime_str, '%Y%m%d%H%M%S')
        except (IndexError, ValueError) as e:
            # Если ошибка парсинга - используем дату создания файла
            date = datetime.fromtimestamp(os.path.getctime(filepath))
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        reports.append({
            'filename': filename,
            'content': content,
            'date': date
        })
    
    # Сортируем по дате (новые сверху)
    return sorted(reports, key=lambda x: x['date'], reverse=True)

@main_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            data = {field: request.form.get(field, '') for field in [
                'name', 'expected_level', 'attendance',
                'topic', 'difficulty', 'grade',
                'assigned_date', 'due_date', 'submission_date'
            ]}
            
            if not data['name'] or not data['topic']:
                raise ValueError("Обязательные поля: Имя и Тема работы")
                
            save_report(data)
            return redirect(url_for('main_bp.analysis', success=True))
            
        except Exception as e:
            return render_template("index.html", error=str(e))
    
    return render_template("index.html")

@main_bp.route("/analysis")
def analysis():
    reports = get_all_reports()
    success = request.args.get('success', 'false') == 'true'
    return render_template("analysis.html", 
                         reports=reports,
                         success=success)