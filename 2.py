print("Оцените нашу программу от 0 до 5: ")
estimation = float(input())

if  5.0 <= estimation or  4.5 < estimation  :
    print("Отлично ⭐⭐⭐⭐⭐")
elif 4.5 <= estimation or estimation > 3.5 :
    print("Хорошо ⭐⭐⭐⭐ ")
elif 3.5 <= estimation or estimation > 2.5 :
    print("Нормально ⭐⭐⭐ ")
elif 2.5 <= estimation or estimation > 1.5 :
    print("Плохо ⭐⭐ ")
elif 1.5 <= estimation or estimation > 0.0 :
    print("Ужасно ⭐ ")
else:
    print("Вы не оценили :(")