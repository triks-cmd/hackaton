def get_feedback(performance_label, grade, attendance, assignment_rate):
    feedback = []
    
    if performance_label == 3:
        feedback.append("Отличная успеваемость! Ваши результаты выше всех ожиданий.")
        feedback.append("Совет: продолжайте в том же духе и делитесь своими знаниями с однокурсниками.")
    elif performance_label == 2:
        feedback.append("Хорошая успеваемость, но есть потенциал для роста.")
        feedback.append("Совет: уделяйте больше внимания сложным темам и практическим заданиям.")
    elif performance_label == 1:
        feedback.append("Успеваемость удовлетворительная, но требует улучшения.")
        feedback.append("Совет: пересмотрите учебный план и обратитесь за помощью к преподавателям.")
    else:
        feedback.append("Низкая успеваемость. Необходимо срочно пересмотреть методику обучения.")
        feedback.append("Совет: разработайте индивидуальный план обучения и уделяйте больше внимания практическим заданиям.")
    
    if attendance < 75:
        feedback.append("Низкая посещаемость может негативно сказаться на усвоении материала. Старайтесь посещать занятия регулярно.")
    else:
        feedback.append("Хорошая посещаемость помогает лучше усваивать материал.")
    
    if assignment_rate < 0.75:
        feedback.append("Низкий процент выполнения домашних заданий. Рекомендуется выполнять все задания вовремя для закрепления материала.")
    else:
        feedback.append("Отличное выполнение домашних заданий помогает закрепить знания.")
    
    return "\n".join(feedback)
