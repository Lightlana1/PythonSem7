import random
from random import randint

# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
__all__ = ['fill_file']

MIN = -1000
MAX = 1000


def fill_file(file_name="names.txt", limit=MAX):
    with open(file_name, mode="w", encoding="utf-8") as file:
        for _ in range(limit + 1):
            first_int: int = randint(MIN, MAX)
            second_double: float = round(random.uniform(-1000, 1000), 2)
            file.write(f"{first_int} | {second_double} \n")

fill_file()
