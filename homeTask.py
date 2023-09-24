        
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.

file_path = 'phone_book.txt'

def add_contact(file_path):
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')


    with open(file_path, 'a') as file:
        file.write(f'{surname}, {name}, {patronymic}, {phone}n')
    

def display_contacts(file_path):
    with open(file_path,  'r') as file:
        for line in file:
            print(line.strip())


def search_contact(file_path):
    search_query = input('Введите имя, фамилию или отчество для поиска: ')

    with open(file_path, 'r') as file:
        for line in file:
            if search_query.lower() in line.lower:
                print(line.strip())


def change_contact(file_path):
    surname = input('Введите фамилию записи, которую нужно изменить: ')
    name = input('Введите имя записи, которую нужно изменить')

    new_surname = input('Введите новую фамилию: ')
    new_name = input('Введите новое имя: ')
    new_patronymic = input('Введите новое отчество: ')
    new_phone = input('Введите новый телефон: ')

    with open(file_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if surname.lower()  in line.lower() and name.lower() in line.lower():
                file.write(f'{new_surname}, {new_name}, {new_patronymic}, {new_phone}n')
            else:
                file.write(line)
        file.truncate()

def delete_contact(file_path):
    surname = input('Введите фамилию записи, которую нужно удалить: ')
    name = input('Введите имя записи, которую нужно удалить: ')

    with open(file_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if surname.lower() not in line.lower() or name.lower() not in line.lower():
                file.write(line)
        file.truncate()


add_contact(file_path)
display_contacts(file_path)
search_contact(file_path)
change_contact(file_path)
delete_contact(file_path)


# Задача 34:  Винни-Пух попросил Вас посмотреть,
# есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке




# song = input()
# vowels = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
# parts = song.split()
# itog = list()

# for item in parts:
#     k = 0
#     for letter in item:
#         if letter in vowels:
#             k += 1
#     itog.append(k)
   
# if len(set(itog)) == 1:
#     print('Парам пам-пам')
# else:
#     print('Пам парам')



#Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, 
# как, например, у операции умножения.


# def print_operation_table(operation, num_rows, num_columns):
#   for i in range(1, num_rows+1):
#     for j in range(1, num_rows+1):
#       result = operation(i, j)
#       print(operation(i, j), end='\t')
#     print()
      

# print(print_operation_table(lambda i, j: i * j, 6, 6))










# Задача 30:  Заполните массив элементами арифметической прогрессии. 

# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
#     print(a1 + i * d, end=' ')

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# from random import randint
 
# lo, hi = 3, 8
# data = [randint(1, 10) for _ in range(20)]
# print("Массив:", data, sep='\n')
# indexes = [i for i, v in enumerate(data) if lo <= v <= hi]
# print("Индексы элементов в заданном диапазоне:", indexes, sep='\n')
# result = []




# Задача 22:
#  Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# n=(int(input("Введите число N элементов: ")))
# num_list_1=[]
# for i in range(n):
#     num = int(input("Введите num "))
#     num_list_1.append(num)
# print(num_list_1)


# m=(int(input("Введите число M элементов: ")))
# num_list_2 = []
# for i in range(m):
#     num = int(input("Введите num "))
#     num_list_2.append(num)
# print(num_list_2)

# num_list_3 = []
# num_list_3 = list(set(num_list_1) & set(num_list_2))
# print(num_list_3)





# # Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
#  Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
#  Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым
#  кустом заданной во входном файле грядки.

# n = int(input('Введите количество кустов черники: '))
# arr = []
# for i in range(n):
#     a =int(input('Введите количество ягод на кусте: '))
#     arr.append(a)

# arr_count = []
# for i in range(len(arr)):
#        arr_count.append(arr[i-2] + arr[i-1] + arr[i])
# print(f'максимальное количество ягод с трёх кустов {(max(arr_count))}')