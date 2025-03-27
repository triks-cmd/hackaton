from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
import os
import glob

main_bp = Blueprint('main_bp', __name__)

REPORTS_DIR = 'reports'

def save_report(data):
    """Сохраняет полный отчет в файл"""
    os.makedirs(REPORTS_DIR, exist_ok=True)
    filename = f"{REPORTS_DIR}/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=== Данные студента ===\n")
        f.write(f"Имя: {data['name']}\n")
        f.write(f"Ожидаемый уровень: {data['expected_level']}\n")
        f.write(f"Посещаемость: {data['attendance']}%\n\n")
        
        f.write("=== Данные работы ===\n")
        f.write(f"Тема: {data['topic']}\n")
        f.write(f"Сложность: {data['difficulty']}\n")
        f.write(f"Оценка: {data['grade']}\n")
        f.write(f"Дата выдачи: {data['assigned_date']}\n")
        f.write(f"Срок сдачи: {data['due_date']}\n")
        f.write(f"Дата сдачи: {data['submission_date']}\n")

def get_all_reports():
    """Возвращает все сохраненные отчеты"""
    reports = []
    for filepath in glob.glob(f"{REPORTS_DIR}/*.txt"):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        reports.append({
            'filename': os.path.basename(filepath),
            'content': content,
            'date': filepath.split('_')[1].split('.')[0]  # Извлекаем дату из имени файла
        })
    # Сортируем по дате (новые сверху)
    return sorted(reports, key=lambda x: x['date'], reverse=True)

@main_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            report_data = {
                # Данные студента
                "name": request.form.get("name", "").strip(),
                "expected_level": request.form.get("expected_level", "").strip(),
                "attendance": request.form.get("attendance", "").strip(),
                
                # Данные работы
                "topic": request.form.get("topic", "").strip(),
                "difficulty": request.form.get("difficulty", "").strip(),
                "grade": request.form.get("grade", "").strip(),
                "assigned_date": request.form.get("assigned_date", "").strip(),
                "due_date": request.form.get("due_date", "").strip(),
                "submission_date": request.form.get("submission_date", "").strip()
            }
            
            if not report_data["name"] or not report_data["topic"]:
                raise ValueError("Заполните обязательные поля (Имя и Тема)")
                
            save_report(report_data)
            return redirect(url_for('main_bp.analysis', success=True))
            
        except Exception as e:
            return render_template("index.html", error=str(e))
    
    return render_template("index.html")

@main_bp.route("/analysis")
def analysis():
    success = request.args.get('success', 'false') == 'true'
    reports = get_all_reports()
    return render_template("analysis.html", success=success, reports=reports)