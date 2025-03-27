from flask import Blueprint, render_template, request, redirect, url_for
import os
import requests
from dotenv import load_dotenv

load_dotenv()

main_bp = Blueprint('main_bp', __name__)

def send_to_telegram(message):
    try:
        bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        chat_id = os.getenv('TELEGRAM_CHAT_ID')
        
        if not bot_token or not chat_id:
            raise ValueError("Не заданы Telegram токен или chat_id")
            
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        response = requests.post(url, json={
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "HTML"
        })
        
        return response.status_code == 200
        
    except Exception as e:
        print(f"Ошибка отправки в Telegram: {e}")
        return False

@main_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            student_name = request.form.get("name", "").strip()
            grade = request.form.get("grade", "").strip()
            
            if not student_name or not grade:
                raise ValueError("Заполните все обязательные поля")
            
            message = f"""
            <b>Новый отчет студента</b>
            👤 Имя: {student_name}
            ⭐ Оценка: {grade}
            """
            
            success = send_to_telegram(message)
            return redirect(url_for('main_bp.analysis', success=success))
            
        except Exception as e:
            return render_template("index.html", error=str(e))
    
    return render_template("index.html")

@main_bp.route("/analysis")
def analysis():
    success = request.args.get('success', 'false') == 'true'
    return render_template("analysis.html", success=success)