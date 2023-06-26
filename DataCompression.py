# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 17:39:10 2022

@author: Shadrina Maria
"""

"Сжатие данных. Текст"

""" Алгоритм арифметического сжатия текста.
При сжатии текстовой информации вычисляется вероятность появления символов
в тексте. Рассчитываются интервалы вероятностей появления символов. Задается 
диапазон [0,0 - 1,0), в котором в зависимости от исходного количества символов 
в тексте определяются промежутки по формуле для левой границы:
"начало диапазона + длина диапазона * левая вероятность появления символа",
для правой границы:
"начало диапазона + длина диапазона * левая вероятность появления символа".
В полученном диапазоне определеятся конечное число - сжатая 
информация, которая поддается декодированию. 

Алгоритм арифметического восстановления текста:
При восстановлении текста число, его кодирующее, определяет первый символ.
Далее по формуле находятся следующие символы:
"Деление разности из числа раскодированного символа левой границы интервала 
раскодированного символа на разность из правой границы интервала 
раскодированного символа его левой границы"
"""

"Получение интервала доступных значений для кодирования текста"
def interval_value_text_code(text):
    counts = []
    symbols= []
    "заполнение массива 1-ми для подсчета частот появления в тексте"
    for i in range(len(text)):
        counts.append(1)
    "Подсчет частот появления символов в тексте"
    for l in range(len(text)):
        for i in range(len(text)):
            if l < i and counts[i] != 0:
                if text[l] == text[i]:
                    counts[l] = counts[l] + 1
                    counts[i] = 0
        "Заполнение массива неповторяющимися значениями символов"
        if counts[l] >= 1:
            symbols.append(text[l])
    "Удаление из массива 0-х значений"
    for i in range(counts.count(0)):
        counts.remove(0)
    "print(counts). Подсчет вероятности появления символов в тексте"
    for i in range(len(counts)):
        counts[i] = round(counts[i] / len(text), 5)
        
    "Заполнение интервалов вероятностей появления символов"
    intervals = [0.0]
    sum = 0.0
    "Заполнение интервалов вероятностей"
    for i in range(len(counts)):
        intervals.append(round(sum + counts[i], 4))
        sum = sum + counts[i]

    "Определение исходного интервала по 1 символу"
    for s in range(len(symbols)):
        if text[0] == symbols[s]:
            interval = [intervals[s], intervals[s + 1]]
    "Расчет итогого диапазона для кодирования текста"
    "Длина первого интервала"
    d = interval[1] - interval[0]
    for s_t in range(len(text) - 1):
        for s in range(len(symbols)):
            if text[s_t + 1] == symbols[s]:
                "Границы нового интервала"
                interval[1] = interval[0] + intervals[s + 1] * d
                interval[0] = interval[0] + intervals[s] * d
                d = interval[1] - interval[0]
    return interval, symbols, len(text)

"Восстановление текста"
def text_recovery(value, symbols, intervals, len_text):
    t = ''
    "Для исключения попадания в лишние диапазоны, создаем переменную памяти"
    val = value
    for k in range(len_text):
        for i in range(len(intervals)):
            if value == val:
                "Число, входящее в диапазон, определяет следующий символ"
                if intervals[i] <= value < intervals[i + 1]:
                    val = (value-intervals[i])/(intervals[i+1]-intervals[i])
                    t = t + symbols[i]
        value = val
    return t

"""
"Универсальная функция извлечения данных"
def extract_data(data):
    
    return
"""
text = 'qwerty uiopasdf'
data_text = interval_value_text_code(text)
print(data_text) 

#recovery_ text = text_recovery(value_text, 
#['q', 'w', 'e', 'r', 't', 'y', ' ', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f'], 
#[0.0, 0.0667, 0.1333, 0.2, 0.2667, 0.3333, 0.4, 0.4667, 0.5334, 
#0.6, 0.6667, 0.7334, 0.8, 0.8667, 0.9334, 1.0], 15)

















