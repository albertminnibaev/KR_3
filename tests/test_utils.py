
from utils import utils

import pytest


@pytest.fixture
def coll():
    return [{
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
    },
    {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
    }]

def test_get_data(coll):
    assert utils.get_data(coll[0]) == '03.07.2019'

def test_get_data(coll):
    assert utils.get_data(coll[1]) == '23.03.2018'

def test_teaching_purpose_of_payment(coll):
    assert utils.teaching_purpose_of_payment(coll[0]) == 'MasterCard 7158 30** **** 6758 -> Счет **5560'
    assert utils.teaching_purpose_of_payment(coll[1]) == 'Счет **2431'

def test_get_amount(coll):
    assert utils.get_amount(coll[0]) == '8221.37 USD'

def test_coding(coll):
    assert utils.coding(coll[0]['from']) == 'MasterCard 7158 30** **** 6758'
    assert utils.coding(coll[1]['to']) == 'Счет **2431'

def test_get_list_of_recent_operations():
    assert utils.get_list_of_recent_operations() == [
        {'id': 863064926,
         'state': 'EXECUTED',
         'date': '2019-12-08T22:46:21.935582',
         'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Открытие вклада',
         'to': 'Счет 90424923579946435907'},
        {'id': 114832369,
         'state': 'EXECUTED',
         'date': '2019-12-07T06:17:14.634890',
         'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации',
         'from': 'Visa Classic 2842878893689012',
         'to': 'Счет 35158586384610753655'},
        {'id': 154927927, 'state': 'EXECUTED',
         'date': '2019-11-19T09:22:25.899614',
         'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод организации',
         'from': 'Maestro 7810846596785568',
         'to': 'Счет 43241152692663622869'},
        {'id': 482520625,
         'state': 'EXECUTED',
         'date': '2019-11-13T17:38:04.800051',
         'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод со счета на счет',
         'from': 'Счет 38611439522855669794',
         'to': 'Счет 46765464282437878125'},
        {'id': 801684332,
         'state': 'EXECUTED',
         'date': '2019-11-05T12:04:13.781725',
         'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Открытие вклада',
         'to': 'Счет 77613226829885488381'}
    ]