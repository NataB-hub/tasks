"""
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов,
на которые есть ссылка.
Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов,
которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением
случаев с относительными ссылками вида
<a href="../some_path/index.html">.
Сайты следует выводить в алфавитном порядке.
Пример HTML файла:
<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">
Пример ответа:
mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru
"""
import re
import requests

"""Блок, где получаем и записываем в файл весь документ html """
# link = input()
# res = requests.get(link)
# with open("hrefs.html", "w") as file_html:
#     file_html.write(res.text)


hrefs = []
pattern = r"<a.+\bhref=[\"|\'](?:\w+.\:\/\/)?(\w[\w.-]+)"
with open("hrefs.html", "r") as file_href:
    for line in file_href:
        hrefs.extend(re.findall(pattern, line))
a = list(set(hrefs))
a.sort()
print('\n'.join(a))
