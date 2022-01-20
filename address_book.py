from pprint import pprint
import csv 
import requests
import re
url = 'https://raw.githubusercontent.com/netology-code/py-homeworks-advanced/master/5.Regexp/phonebook_raw.csv'
with open('phonebook_raw.csv', 'w') as f:
  data = requests.get(url)
  new_data = data.text
  f.write(new_data)
  

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

# # TODO 1: выполните пункты 1-3 ДЗ
#task 1
condition_names = r'(([А-Я]{1}[а-я]+)(\,?)\s?([А-Я]{1}[а-я]+)?(\,|\s?)([А-Я]{1}[а-я]+)(\,?)\s?(\,?)\s?(\,?)\s?'
substitution_names = r'\1,\3,\5,'
result_names = re.sub(condition_names, substitution_names, contacts_list)
#task 2
condition_phone = (r'(8|\+7)\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})*\-*(\d{2})\s*\(*(доб.)*\s*(\d+)*')
substitution_phone = (r'+7(\2)\3-\4-\5 \6\7')
result_phone = re.sub(condition_phone, substitution_phone, contacts_list)
print(result_names)

# # TODO 2: сохраните получившиеся данные в другой файл
with open ('phonebook_new version.csv', 'w') as f:
  f.write(result_names)

# # код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)

