import re
from pprint import pprint

# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# print(contacts_list)
# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
pattern_pfone = r'[\+7|8]*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d{4})*[\)]*'
pattern_sub = r'+7(\1)-\2-\3-\4 \5\6'


def get_contacts_list(contacts_list):
    new_contacts_list = list()
    for item in contacts_list:
        full_name = ' '.join(item[:3]).split(' ')
        result = [full_name[0], full_name[1], full_name[2], item[3], item[4],
                  re.sub(pattern_pfone, pattern_sub, item[5]).strip(), item[6]]
        new_contacts_list.append(result)
    return new_contacts_list


# pprint(get_contacts_list(contacts_list))

def sort_contacts_list(contacts_list):
    contacts = get_contacts_list(contacts_list)
    for contact in contacts:
        first_name = contact[0]
        last_name = contact[1]
        for double_contact in contacts:
            double_first_name = double_contact[0]
            double_last_name = double_contact[1]
            if first_name == double_first_name and last_name == double_last_name:
                if contact[2] == '':
                    contact[2] = double_contact[2]
                if contact[3] == '':
                    contact[3] = double_contact[3]
                if contact[4] == '':
                    contact[4] = double_contact[4]
                if contact[5] == '':
                    contact[5] = double_contact[5]
                if contact[6] == '':
                    contact[6] = double_contact[6]

    result_list = list()
    for i in contacts:
        if i not in result_list:
            result_list.append(i)
    # pprint(result_list)
    return result_list


if __name__ == '__main__':
    result = sort_contacts_list(contacts_list)
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(result)
