
# Импорт функций из файла utils из папки utils
from utils.utils import get_list_of_recent_operations, get_data, teaching_purpose_of_payment, get_amount


def main():
    """
    Основной блок программы, выводит информацию о последних пяти оперциях
    :return: последние пять оперций
    """
    print(get_list_of_recent_operations())
    for elem in get_list_of_recent_operations():
        print(f"{get_data(elem)} {elem['description']}")
        print(f"{teaching_purpose_of_payment(elem)}")
        print(f"{get_amount(elem)}\n")


if __name__ == '__main__':
    main()

