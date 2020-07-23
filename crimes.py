"""
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года
по настоящее время.
Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
Файл с данными:
Crimes.csv
"""
import csv

dict_type = dict()
with open("Crimes.csv", "r") as table:
    reader = csv.reader(table)
    for line in reader:
        if "2015 " in line[2]:
            if line[5] in dict_type:
                dict_type[line[5]] += 1
            else:
                dict_type.update({line[5]: 1})
most_type = max([[value, key] for key, value in dict_type.items()])
print(most_type[1])
