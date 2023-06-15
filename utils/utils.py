
# импорт используемых библиотек
import os
import json
from datetime import datetime


# сохранение пути к файлу 'operations.json' в переменную operations_json
#operations_json = os.path.join('..', 'data', 'operations.json')
operations_json = os.path.join('data', 'operations.json')


def get_list_of_recent_operations():
    """
    Формирует из файла 'operations.json' список с 5 последними операциями
    :return: список с 5 последними операциями упорядоченный по дате
    """
    with open(operations_json, encoding="utf-8") as file:
        operations_list = json.load(file)
    operations_list_date = [i['date'] for i in operations_list if i and i["state"] == "EXECUTED"]
    operations_list_date.sort(reverse=True)
    list_of_recent_operations = []
    for elem in operations_list:
        if elem and elem['date'] in operations_list_date[0:5]:
            list_of_recent_operations.append(elem)
    list_of_recent_operations.sort(key=lambda k: k['date'], reverse=True)
    return list_of_recent_operations


def get_data(element):
    """
    Получает на вход информацию об одной операции и выводит дату оперции в формате 08.12.2019
    :param element: информация об одной операции
    :return: дата оперции в формате 08.12.2019
    """
    date = datetime.strptime(element['date'], '%Y-%m-%dT%H:%M:%S.%f')
    return date.date().strftime('%d.%m.%Y')


def coding(element):
    """
    Получает на вход информацию об одной операции и выводит скрытые реквезиты счетов и карт перевода
    в виде Visa Classic 2842 87** **** 9012 или Счет **3655
    :param element: информация об одной операции
    :return: скрытая информацию о счетах и картах перевода в виде Visa Classic 2842 87** **** 9012 или
     Счет **3655
    """
    name_score = " ".join(element.split()[:-1])
    namber_score = element.split()[-1]
    if name_score == "Счет":
        namber_score_code = f"**{namber_score[-4:]}"
    else:
        namber_score_code = f"{namber_score[:4]} {namber_score[4:6]}** **** {namber_score[-4:]}"
    return f"{name_score} {namber_score_code}"


def teaching_purpose_of_payment(element):
    """
    Получает на вход информацию об одной операции и выводит информацию о счетах перевода
    в виде Visa Classic 2842 87** **** 9012 -> Счет **3655
    :param element: информация об одной операции
    :return: информацию о счетах перевода в виде Visa Classic 2842 87** **** 9012 -> Счет **3655
    """
    if 'from' in element:
        return f"{coding(element['from'])} -> {coding(element['to'])}"
    else:
        return f"{coding(element['to'])}"

def get_amount(element):
    """
    Получает на вход информацию об одной операции и выводит сумму перевода
    :param element: информация об одной операции
    :return: сумма перевода
    """
    return f"{element['operationAmount']['amount']} {element['operationAmount']['currency']['name']}"
