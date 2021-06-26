from pprint import pprint
import csv 
import requests
import re
# url = 'https://raw.githubusercontent.com/netology-code/py-homeworks-advanced/master/5.Regexp/phonebook_raw.csv'
# with open('phonebook_raw.csv', 'w') as f:
#   data = requests.get(url)
#   new_data = data.text
#   f.write(new_data)
  
  


# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# # TODO 1: выполните пункты 1-3 ДЗ
# # ваш код
result = re.findall(condition, contacts_list)

# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)

