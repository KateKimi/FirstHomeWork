"""
Задание 1. Со значениями по умолчанию
Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:

1-е число – сколько строк будет в песне. По умолчанию 3
2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
3-е число – если 0, то в конце песни (в конце последней строчки) стоит точка, если 1, то в конце стоит «!». По умолчанию 0

"""

def la_song(row = 3 , word_in_row = 3, in_end = 0):
    word = ["La"]
    song_row = (word * word_in_row)
    s = "-"
    song_row = s.join(song_row)
    nl = '\n'
    all_song = f"{nl}{song_row}"
    if in_end == 0:
        my_song = f"{all_song * row}."
    else:
        my_song = f"{all_song * row}!"
    return my_song
print(la_song())

"""
Задание 2
Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов.
 Учитываем, что может быть повторяющиеся значения аргументов.


"""
def second_maxi():
    my_list = list(input('Enter some numbers: '))
    print(my_list)
    new_list = list(set(my_list))
    return new_list[-2]
print(second_maxi())


"""
Задание 3
Напишите функцию, которая удаляет все небуквенные символы внутри строки (ограничимся латинским алфавитом). 
Проверьте, что вы правильно закодили с помощью инструкции assert.

"""

def notalpha(word):
    b = ""
    for i in word:
        if i.isalpha():
            b = b + i
    return (b)

print(notalpha('hel34lo'))


