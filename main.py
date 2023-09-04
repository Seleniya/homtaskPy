'''
import random
print(random.randint(1,100))
print('Сколько нужно проехать пути?')
a = int(input())


b = int(input('Сколько км вы проедите за день?'))

print(f"{a +( b - 1 ) //b}, столько нужно дней, чтоб проехать {a}км. ")
print("Количество парт = ",(-a // b) *(-1))

print('Ведите год, а я скажу високосный он или нет')

a = int(input())

if (a % 4 == 0 and a % 100 !=0) or (a % 400 == 0):
    print('Это високосный год, 366 дней')
else:
    print('Это невисокосный год, 365 дней')
'''
'''
print('Ведите год, а я скажу високосный он или нет')

a = int(input())
if (a % 4 == 0) and (a % 100 != 0):
    print('Високосный')
elif a % 400 ==0:
    print('Високосный')
else:
    print('Невисокосный')
'''
# a = 400
# print('Yes' if ((a % 4 == 0) and (a % 100 != 0)) or (a % 400 == 0) else 'No')
'''
Задача 2
print('Ведите трёхзначное число, а я посчитаю сумму его цифр')

a = int(input())

b = a // 100
c = (a // 10) % 10
d = a % 10

print(f"Сумма цифр числа {a} = { b + c + d}")

#Задача 4

print('Введите число, кратное 6. Это будет общее количество журавликов.\ А я посчитаю, сколько сделал каждый из детей.')

a = int(input())

b = a // 6 # столько сделал Паша, и Сергей каждый по отдельности
c = b * 4 # столько сделала Катюша

print(f'{b } {c } {b }')


#Задача 6


print('Введите 6ти значное число')

a = int(input())

b = a //100000

c = a //10000 % 10

d = a //1000 % 10

i = a //100 % 10

f = a //10 % 10

g = a % 10


if (b+c+d == i+f+g): print(f'Это счастливый билетик')
else:
    print(f'{a} Это магический билетик, он защитит вас от нападок кондукторов!')
''' 
#Задача 8
'''
m = int(input('Введите длину шоколадки: '))
n = int(input('Введите ширину шоколадки: '))
k = int(input('Можно ли отломать одним разом столько долек? '))


print('Yes' if (m != 0 ) and (n != 0) and (k != 0) and  (k < m * n) and (k % m == 0) or (k % n == 0)   else 'No')
'''
'''
n = int(input())            
count = 1
maxx = 0

for i in range(n):
    temp = int(input())
    if temp > 0:
        count += 1
        maxx = count
    else:          
        count = 0
print(maxx)
'''
'''
n = int(input(f'Введите  общее количество арбузов: ' ))

minn = int(input('Арбуз 1: '))
maxx = minn

for _ in range(n-1):
    temp = int(input('Введите арбуз: '))
    if temp < minn:
        minn = temp
    if temp > maxx:
        maxx = temp
    
print(minn, maxx)
'''
'''
i = 1
while i < 11:
    print(i, end = '')
    i += 1
    continue
    print('NO')
    '''
'''
while (num:=int(input())) < 0:
    print(f'Число {num} маленькое')
'''
'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
n = int(input(f'Введите количество монет: '))
'''
'''
v = int(input(f'Сколько из них лежат решкой? '))
if v < n - v:
    print(f'Нужно перевернуть {v} монет')
else: print(f'Нужно перевернуть {n-v} монет')
'''

'''
Задача 12: Петя и Катя – брат и сестра.
Петя – студент, а Катя – школьница.
Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000),
 а Катя должна их отгадать. Для этого Петя делает две подсказки.
 Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
 '''
'''
S  = int(input('Назовите сумму S  2х чисел: '))
P = int(input('Назовите произведение P 2х чисел: '))
for x in range (P): 
    for y in range (P):
        if (x + y == S) and (x * y == P):
            print(x, y)
'''
'''
Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k), не превосходящие числа N.
'''
'''
N = int(input('Назовите число, а я напишу все степени числа 2, которые попадают в диапазон от 0 до этого числа: '))


i = 0
while N >= 2**i:
    i += 1
    print(2**(i-1), end='  ')


'''   
'''          
my_set = set('Hhhhello') #сделаем множество, без повторов
print(len(my_set))#посчитаем длину списка
'''
'''
str1 = [1, 2, 3, 5, 0, 1, 0]
counter = 0
for i in range(len(str1)):   #
    if str1[i] not in str1[:i]: # если этот i в  этой строке до i отсутствует, тогда счётчик увеличим
        counter += 1
print(counter)
'''
# list = [1, 2, 3, 4, 5, 6]
# k = 1


# for i in range (k):
#     last = list.pop()
#     list.insert(0, last)
# print(list)


# или
# list = [1, 2, 3, 4, 5, 6]
# k = 1
# k = k % len(list)
# print ((list[-k : ]) + (list[: -k] ))



# list = [ {'V': 'S001'},
#     {'B': 'kjio'},
#     {'df': 'sd'},
#     {'er' : 'er'},
#     {'we' : 'er'},
#     {'cv' : 'dc'}]

# my_list = []
   
# for dict in list:
#     for val in dict.values():
#         # print(val)

#         my_list.append(val)
# print(set(my_list))


# for key in dict:
#     print(key)

# for key in dict.keys():
#     print(dict[key])

# for (k, v) in dict.items():
#     print(k, v)


# for item in dict:
#     print('{} : {}'.format(item, dict[item]))

# for val in dict.values():
#     print(val)


# list_1 = [1, 2, 3, 4, 2, 1, 2, 0, 2]
# k = 2


# print(list_1.count(k))





# a=[1, 2, 9, 10, 0, 3]
# x= 4
# b=[abs(a[i]-x) for i in range(len(a))]
# print(a[b.index(min(b))])

# a=[1, 2, 9, 10, 0, 3]
# b= 3
# c=[]  # 2 1 6 7 3 0
# for i in a:
#     c.append(abs(b-i))
# d = c.index(min(c))
# print(a[d])
# list_1=[1, 2, 9, 10, 0, 3]
# k= 11
# b=[abs(list_1[i]-k) for i in range(len(list_1))]
# print(list_1[b.index(min(b))])


# dict = {1 : 'N', 1 : 'O', 1 : 'U', 1 : 'T',  3 : 'B', 5 :'K' }


# dict = {1:'AEIOULNSTR',
#       	2:'DG',
#       	3:'BCMP',
#       	4:'FHVWY',
#       	5:'K',
#       	8:'JZ',
#       	10:'QZ'}

# word = 'DIFFERENT'
#         #   214411111

# print(sum([k for i in word for k, v in dict.items() if i in v]))
	


# list_letters = {1:"AEIOULNSTRАВЕИНОРСТ",
#                 2:"DGДКЛМПУ",
#                 3:"BCMPБГЁЬЯ",
#                 4:"FHVWYЙЫ",
#                 5:"KЖЗХЦЧ",
#                 8:"JXШЭЮ",
#                 10:"QZФЩЪ"}

# word = input("Введите слово: ").upper()
# summ = 0
# for i in word:
#     for k, v in list_letters.items():
#         if i in v:
#             summ += k
# print(summ)


# list_letters = {1:"AEIOULNSTRАВЕИНОРСТ",
#                 2:"DGДКЛМПУ",
#                 3:"BCMPБГЁЬЯ",
#                 4:"FHVWYЙЫ",
#                 5:"KЖЗХЦЧ",
#                 8:"JXШЭЮ",
#                 10:"QZФЩЪ"}
# k = 'ноутбук' #1121322
# word = k.upper()
# sum = 0
# for i in word:
#     for m, v in list_letters.items():
#         if i in v:
#             sum += m
# print(sum)



# all_letters = 'a a b c d d a c l k '.split()

# letters_count = {}
# result_str = ''
# for letter in all_letters:
#     if letter not in letters_count:
#         letters_count[letter] = 1
#         result_str += f'{letter} '
#     else:
#         result_str += f'{letter}_{letters_count[letter]} '
#         letters_count[letter] += 1

# print(result_str)




# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}

# k = 'alla'
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_en:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)



# print(len(set(input().split())))


# max_el = 0

# while (n := int(input())) != 0:
#     if n > max_el:
#         max_el = n
# print(max_el)



'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
n = int(input(f'Введите количество монет: '))
'''
'''
v = int(input(f'Сколько из них лежат решкой? '))
if v < n - v:
    print(f'Нужно перевернуть {v} монет')
else: print(f'Нужно перевернуть {n-v} монет')
'''

'''
Задача 12: Петя и Катя – брат и сестра.
Петя – студент, а Катя – школьница.
Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000),
 а Катя должна их отгадать. Для этого Петя делает две подсказки.
 Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
 '''
'''
S  = int(input('Назовите сумму S  2х чисел: '))
P = int(input('Назовите произведение P 2х чисел: '))
for x in range (P): 
    for y in range (P):
        if (x + y == S) and (x * y == P):
            print(x, y)
'''
'''
Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k), не превосходящие числа N.
'''
# N = int(input('Назовите число, а я напишу все степени числа 2, которые попадают в диапазон от 0 до этого числа: '))


# i = 0
# while N >= 2**i:
#     i += 1
#     print(2**(i-1), end='  ')
