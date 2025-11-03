"""
Простая программа для определения заболевания: Грипп или Ангина
"""

def main():
    print("=" * 50)
    print("ДИАГНОСТИКА ЗАБОЛЕВАНИЙ")
    print("=" * 50)
    print("Ответьте на вопросы о симптомах (да/нет)\n")
    
    # Сбор симптомов
    symptoms = {}
    
    symptoms['temperature'] = input("Температура выше 38°C? (да/нет): ").lower().strip() in ['да', 'д', 'yes', 'y']
    symptoms['body_pain'] = input("Сильная ломота в теле? (да/нет): ").lower().strip() in ['да', 'д', 'yes', 'y']
    symptoms['throat_pain'] = input("Сильная боль в горле? (да/нет): ").lower().strip() in ['да', 'д', 'yes', 'y']
    symptoms['weakness'] = input("Сильная слабость? (да/нет): ").lower().strip() in ['да', 'д', 'yes', 'y']
    
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТ ДИАГНОСТИКИ:")
    print("=" * 50)
    
    # Логика диагностики
    flu_score = sum([symptoms['temperature'], symptoms['body_pain'], symptoms['weakness']])
    angina_score = sum([symptoms['temperature'], symptoms['throat_pain']])
    
    if flu_score >= 2 and flu_score > angina_score:
        print("Вероятный диагноз: ГРИПП")
        print("\nРекомендации:")
        print("- Постельный режим")
        print("- Обильное питье")
        print("- Вызвать врача")
        
    elif angina_score >= 2 and angina_score > flu_score:
        print("Вероятный диагноз: АНГИНА")
        print("\nРекомендации:")
        print("- Полоскание горла")
        print("- Обратиться к врачу")
        
    else:
        print("Не удалось точно определить заболевание")
        print("Рекомендуется обратиться к врачу")
    
    print("\n" + "=" * 50)
    print("ВАЖНО: Это учебная программа!")
    print("Для точного диагноза обратитесь к врачу.")
    print("=" * 50)

if __name__ == "__main__":
    main()
