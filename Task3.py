# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

__all__ = ['read_file']

def read_file(file_name="result_num_names.txt"):
    with open("../names.txt", mode="r", encoding="utf-8") as numbers, \
         open("../names_rand.txt", mode="r", encoding="utf-8") as name_file, \
         open(file_name, mode="w", encoding="utf-8") as result_file:

        len_name = 0
        len_num = 0

        numbers_list = []
        names_list = []

        for num in numbers:
            a, b = map(float, num.split("|"))
            numbers_list.append(a*b)
            len_num += 1
        print(numbers_list)
        print(len_num)

        for name in name_file:
            names_list.append(name[:-1])
            len_name+=1
        print(names_list)

        if len_num > len_name:

            for i in range(len(numbers_list)):
                with open("../names_rand.txt", mode="r", encoding="utf-8") as name_file:
                    for line in name_file:
                        try:
                            result_file.write(f"{line[:-1]} = {round(numbers_list[i], 2)} \n")
                        except StopIteration:
                            name_file.seek(0)


read_file()
