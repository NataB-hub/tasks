"""
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле
name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Эквивалент на Python:
class A:
    pass
class B(A, C):
    pass
class C(A):
    pass
Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно
от одного класса более одного раза.
Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
<имя класса> : <количество потомков>
Выводить классы следует в лексикографическом порядке.
Sample Input:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Sample Output:
A : 3
B : 1
C : 2
"""
import json

"""функция, ктр ищет всех родственником для одного класса"""
def sean(relative, all_connection):
    for one_family in family_work:
        if relative in one_family["parents"]:
            if one_family["name"] not in all_connection:
                all_connection.append(one_family["name"])
            sean(one_family["name"], all_connection)
    return all_connection


family_work = json.loads(input())

listrelatives, finish = [], {}
for one_parents in family_work:
    w = sean(one_parents["name"], listrelatives)
    finish[one_parents["name"]] = (len(w) + 1)
    listrelatives = []
for key, value in sorted(finish.items()):
    print(f'{key} : {value}')

