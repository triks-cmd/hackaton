from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph

def generate_student_report(student):
    filename = f"reports/{student.name}_report.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    
    styles = getSampleStyleSheet()
    width, height = A4
    
    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height-50, f"Report for {student.name}")
    
    # Content
    text = f"""
    <b>Overall Performance:</b> {student.calculate_final_level()}%
    <b>Attendance:</b> {student.attendance}%
    """
    p = Paragraph(text, styles["Normal"])
    p.wrapOn(c, 400, 50)
    p.drawOn(c, 50, height-150)
    
    c.save()
    return filename