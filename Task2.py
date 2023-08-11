# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
__all__ = ['write_rand_names', 'gener_random_names']
import random
import string

MIN = 4
MAX = 7

def gener_random_names()-> str :
    names_list = string.ascii_lowercase
    length: int = random.randint(MIN, MAX-1)
    upper_names = string.ascii_uppercase
    rand_string = []
    rand_string.append(random.choice(upper_names))
    print(length)
    print(rand_string)
    vowels = ['a', 'o', 'e', 'i', 'u', 'y']
    flag = False


    while flag != True:
        while length>0:
            rand_string.append(random.choice(names_list))
            length-=1
        for i in range (len(vowels)):
            if vowels[i] in rand_string:
                flag = True

    str_name = ''.join(rand_string)
    return str_name



def write_rand_names(str_name: str, file_name="names_rand.txt"):
    with open(file_name, mode="a", encoding="utf-8") as file:
        file.write(f"{str_name} \n")


if __name__ == '__main__':
    name_random = gener_random_names()
    write_rand_names(name_random)



