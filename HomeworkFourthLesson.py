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

x = int(input("Please enter integer: "))
a = 0
while x % 2 == 0:
    x = x // 2
    print(x)
if x % 2 != 0:
    print("Not integer")





