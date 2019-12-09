#First task from fourth homework

# try:
#     x = input("Enter text: ")
#     print(x)
#     print(x[2], x[-2], x[0:5], x[::2], x[1::2], x[::-1], x[-1::-2], x[-2::-2], len(x), sep="\n")
# except IndexError:
#     print("Exception: Текст короче допустимого")


# Second task in homework (fourth lesson)
    # 1 part of task
#
# l = 0
# while l < 10:
#     l = l + 1
#     print(l)

    # 2 part of task

# l = 20
# while l > 0:
#     l = l - 1
#     print(l, end=' ')

    # 3 part of task without 'Посчитайте сколько раз вы делили нацело на 2. '

# x = int(input("Please enter integer: "))
# a = 0
# while x % 2 == 0:
#     x = x // 2
#     print(x)
#     a = a + 1
# if x % 2 != 0:
#     print("Not integer")
# print("Итоговое количество чётных итераций: ", a)


#Third task of homework

        # 1 part of the task
# a = [1, 2, 3, 4, 5]
# while a:
#     print(a.pop(0))
#     print(a)

        #2 part of the task

# a = 'hello'
# while a:
#     a = a[1:]
#     print(a)

        #3 part of the task (3.	Напишите цикл, который выводит на экран и удаляет элементы списка
                            # от самого маленького до самого большого, пока он не останется пустым)

# a = [1, 5, 3, 6, 8]
# a= sorted(a)
# print(sorted(a))
# while a:
#     a = a[1:]
#     print(a)


#Fourth task of homework
                # 1 part of the task
# a = ['hello', 23, 'apple', [21, 15], 48, (12, 15)]
# countint = 0
# countstr = 0
# countlist = 0
# countdic = 0
# counttuple = 0
# for i in a:
#     if type(i) is int:
#         print(i)
#         countint = countint + 1
#     elif type(i) is list:
#         print(i)
#         countlist = countlist + 1
#     elif type(i) is str:
#         print(i)
#         countstr = countstr + 1
#     elif type(i) is dict:
#         print(i)
#         countdic = countdic + 1
#     elif type(i) is tuple:
#         print(i)
#         counttuple = counttuple + 1
#
# print("Int:", countint, "Str:", countstr, "List:", countlist, "Dictionary:", countdic, "Tuple:", counttuple)

            #2 part of the task. 2. * Дана последовательность чисел.
            # Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.

# a = [1, 2, 2, 3, 4, 5, 5, 5, 24, 24, 6, 6, 6, 6]
# b = -1
# count = 0
# max_count = 0
# for i in a:
#     if b == i:
#         count = count + 1
#     else:
#         b = i
#         max_count = max(count, max_count)
#         count = 1
# max_count = max(count, max_count)
# print(max_count)

#Fifth Task in homework

# a = input("Enter number: ")
# b = input("Enter second number: ")
#
# try:
#     print(int(a) + int(b))
# except ValueError:
#     print(a + b)

# 6 task in homework
#1)	Пишем функцию, которая попросит ввести число. Пока он не введёт правильно, просите его ввести.
# Функция возвращает введённое число.
#* Теперь далее для других задач с числами, вы можете пользоваться этой функцией, а не простым input!

# def vvod_number():
#     while True:
#         x = input("Enter a number")
#         try:
#             return int(x)
#         except ValueError:
#             print("It is not a number")
# vvod_number()

#2)	Пишем функцию, которая попросит пользователя ввести слово (строка без пробелов в середине, а вначале и в конце пробелы могут быть).
# Пока он не введёт правильно, просите его ввести. Функция возвращает введённое слово.

# def vvod_word():
#     while True:
#         x = input("Enter a word ").strip()
#         if x.isalpha():
#             return x
#         else:
#             print("It is not a word")
# vvod_word()

#Это уже было в предыдущем ДЗ, но теперь оформите это функцией:
#  3)	Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе


def is_year_leap(year):
    year =int(year)
    if ((year % 4 == 0) and (year % 100 !=0)) or (year % 400 == 0):
        return True
    else:
        return False
if __name__ == "__main__":
    print(is_year_leap(2016))

#4)	Функция принимает три числа a, b, c.
# Функция должна определить, существует ли треугольник с такими сторонами. Если треугольник существует, вернёт True, иначе False.

# def my_triangle(a, b, c):
#     a = int(a)
#     b = int(b)
#     c = int(c)
#     if (a + b) > c and (a + c) > b and (b + c) > a:
#         return True
#     else:
#         return False
# print(my_triangle(5, 6, 7))

#5)	Функция принимает три числа a, b, c.
# Функция должна определить, существует ли треугольник с такими сторонами и если существует,
# то возвращает тип треугольника Equilateral triangle (равносторонний),
# Isosceles triangle (равнобедренный), Versatile triangle (разносторонний) или не треугольник (Not a triangle).

# def my_triangle(a, b, c):
#     a = int(a)
#     b = int(b)
#     c = int(c)
#     if a == 0 or b == 0 or c == 0:
#         return "Side number can't be '0' "
#     elif (a + b) < c or (a + c) < b or (b + c) < a:
#         return "Not a triangle"
#     else:
#         if a == b == c:
#             return "Equilateral triangle"
#         elif a == b != c or b == c != a or a == c != b:
#             return "Isosceles triangle"
#         elif a != b != c:
#             return "Versatile triangle"
#
# print(my_triangle(2, 2, 4))

#6)	Даны четыре действительных числа: x1, y1, x2, y2.
# Напишите функцию distance(x1, y1, x2, y2), вычисляющую расстояние между точками с координатами (x1, y1) и (x2, y2).
# Считайте четыре действительных числа от пользователя и выведите результат работы этой функции.

# def distance(x1, y1, x2, y2):
#     return ((x1 + x2) ** 2 + (y1 + y2) ** 2) ** (1 / 2)
# x1 = int(input("Enter number: "))
# y1 = int(input("Enter number: "))
# x2 = int(input("Enter number: "))
# y2 = int(input("Enter number: "))
#
# print('Distance is: ', distance(x1, y1, x2, y2))


#  Seventh task in homework

#Создайте строку, в которой написан, какой-то текст. Пример:
# We are not what we should be!
# We are not what we need to be.
# But at least we are not what we used to be
#  (Football Coach)
# •	Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
# •	Удалите знаки препинания в списке слов (пройдитесь циклом все слова и удалите методом strip знаки препинания)
# •	Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)

# text = 'We are not what we should be!\nWe are not what we need to be.\nBut at least we are not what we used to be.\n(Football Coach)'
# text = text.split()
# print(text)
# for i in range(len(text)):
#     text[i] = text[i].strip("!.(),")
# print(text)
# text.sort(key=str.lower)
# print(text)













