def average_of_temp():
    days_of_list = [1, 2, 10, 25, 'None', 47, 32]
    for i in days_of_list:
        if i == 'None':
            days_of_list.remove('None')
    average = sum(days_of_list) / len(days_of_list)
    return average


result = average_of_temp()
print(result)
