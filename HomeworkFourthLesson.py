#First task from fourth homework

# try:
#     x = input("Enter text: ")
#     print(x)
#     print(x[2], x[-2], x[0:5], x[::2], x[1::2], x[::-1], x[-1::-2], x[-2::-2], len(x), sep="\n")
# except IndexError:
#     print("Exception: Текст короче допустимого")


# Second task in homework (fourth lesson)
    # 1 part of task

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


















