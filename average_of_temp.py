def average_of_temp(days_of_list): #Объявляем функцию
    for i in days_of_list:
        if i == 'None':
            days_of_list.remove('None')
    average = sum(days_of_list) / len(days_of_list)
    return average


l = [1, 2, 10, 25, 'None', 47, 32] # Формируем список для передачи в функцию

average_of_temp(l)  # Передаём список в функцию как параметр

print(average_of_temp(l)) # Выводим результат