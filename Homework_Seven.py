"""
Задание 1 (на создание классов)
Переделываем (а что-то повторяем и закрепляем) наши классы таким образом:
1) Person
(два свойства:
1. теперь full_name пусть будет свойством, а не функцией
(одно поле, мы ожидаем - тип строка и состоит из двух слов «имя фамилия»), а свойств name и surname нету,
2. год рождения).
Реализовать методы, которые:
1.	выделяет только имя из full_name
2.	выделяет только фамилию из full_name;
3.	вычисляет сколько лет было/есть/исполнится в году, который передаётся параметром
 (obj.age_in(year)); если не передавать параметр, по умолчанию, сколько лет в этом году;
** Можете в конструкторе проверить, что в full_name передаётся строка, состоящая из двух слов, если нет, вызывайте исключение 😊
** Можете в конструкторе проверить, что в год рождения меньше 2019 (текущего года), но больше 1900, если нет вызывайте исключение

"""
class Person:
    def __init__(self, full_name=" ", age_birth=None):
        self.full_name = full_name
        if not len(full_name.split(" ")) == 2:
            raise ValueError("Not name and surname")
        self.age_birth = age_birth
        if age_birth > 2019 or age_birth < 1900:
            raise ValueError("Incorrect year")

    def __str__(self):
        return f"{self.__class__} Object: full_name={self.full_name}"

    def only_name(self):
        l = (self.full_name).split()
        name = l[0]
        return name
    def only_surname(self):
        l = (self.full_name).split()
        surname = l[1]
        return surname
    def years(self, year=None):
        import datetime
        if year is None:
            year = datetime.date.today().year
        needed_age = year - self.age_birth
        return needed_age

p1 = Person(full_name="Bob Man", age_birth= 1987)
print(p1.full_name)
print(p1.only_name())
print(p1.only_surname())
print(p1.years())

"""
2) Employee (наследуемся от Person) (добавляются свойства: должность, опыт работы, зарплата)
** Можете в конструкторе проверить, что в опыт работы и зарплата не отрицательные
Реализовать новые методы:
1.	возвращает должность с приставкой, которая зависит от опыта работы: Junior — менее 3 лет, Middle — от 3 до 6 лет, Senior — больше 6 лет.
Т.е. метод должен вернуть позицию с приставкой Junior/Middle/Senior <position>.
 Если, например у вас объект имел должность “programmer” с опытом 2 года, метод должен вернуть “Junior programmer”
2.	метод, который увеличивает зарплату на сумму, которую вы передаёте аргументом.

"""
class Employee(Person):
    def __init__(self, full_name=" ", age_birth=None, salary=None, position=None, experience=None):
        Person.__init__(self, full_name, age_birth)
        # self.full_name = full_name
        # self.age_birth = age_birth
        self.salary = salary
        if salary < 0:
            raise ValueError("Salary can't be < 0")
        self.position = position
        self.experience = experience
        if experience < 0:
            raise ValueError("Experiense can't be < 0")

    def __str__(self):
        return f"{self.__class__} Object: full_name={self.full_name}"

    def mon_position(self):
        experience = self.experience
        if experience < 3:
            m_position = 'Junior'
        elif 3 > experience < 6:
            m_position = 'Middle'
        elif experience > 6:
            m_position = 'Senior'
        return f"{m_position} {self.position}"
    def mon_salary(self, money):
        if type(money) == str or type(money) == list or type(money) == dict:
            raise ValueError('Money must be int or float')
        return self.salary + money


e1 = Employee(full_name="Vasya Man", salary=100, age_birth=1987, experience=2, position='programmer')
print(e1.full_name)
print(e1.mon_position())
print(e1.mon_salary(35))

"""
3) ITEmployee (наследуемся от Employee)
1. Реализовать метод добавления одного навыка в новое свойство skills (список) новым методом add_skill (см. презентацию).
2. * Реализовать метод добавления нескольких навыков в новое свойство skills (список) новым методом add_skills.
Тут можно выбрать разные подходы:
или аргумент один и он список навыков, которым вы расширяете список-свойство skill,
 или вы принимаете неопределённое количество аргументов, и все их добавляете в список-свойство skill
"""
class ITEmployee(Employee):
    def __init__(self, full_name=" ", age_birth=None, salary=None, position=None, experience=None, skills=[]):
        Employee.__init__(self, full_name, age_birth, salary, position, experience)
        self.skills = skills

    def __str__(self):
        return f"{self.__class__} Object: full_name={self.full_name}, skills={self.skills}"

    def add_skills(self, new_skill):
        try:
            self.skills.append(new_skill)
        except AttributeError: self.skills = [new_skill]
        return self.skills

    def all_skills(self, *args):
        for n in args:
            try:
                self.skills.extend(args)
            except AttributeError: self.skills = [*args]
            return self.skills



it1 = ITEmployee(full_name="Petya Man", salary=1000, age_birth=1985, experience=2, position='programmer', skills=[])
print(it1.full_name)
print(it1.add_skills('Java'))
print(it1.all_skills('More','OneMore'))
print(it1.skills)
print(it1.all_skills('Python','Ruby', 'ETC'))

"""
Задание 2 (на создание новых классов)
Создать классы
1) Прямоугольная площадка (пример: комната) (свойства: две стороны).
Методы:
1.	вычисляем площадь,
2.	вычисляем периметр.
3.	** сделайте возможность сливать две «комнаты» в одну операцией +

"""
class Room:
    def __init__(self, one_side, second_side):
        self.one_side = one_side
        self.second_side = second_side

    def __add__(self, other):
        r = Room(self.one_side + other.one_side, self.second_side + other.second_side)
        return r
    def __str__(self):
        return f"Room {self.one_side}, {self.second_side}"

    def S_2(self):
        return self.one_side * self.second_side
    def P(self):
        return ((self.one_side + self.second_side) * 2)

first_room = Room(one_side=5, second_side= 10)

print(first_room.S_2())
print(first_room.P())
room_1 = Room(one_side=5, second_side=10)
room_2 = Room(one_side=8, second_side=9)

all = room_1 + room_2
print(all)

"""
2) Точка на карте (свойства: X, Y). 
Методы:
1.	Нужно вычислить расстояние до начала координат, 
2.	* вычисляется расстояние между точкой и другой точкой экземпляром этого же класса
3.	** перевод в другие системы координат
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        p = Point(self.x + other.x, self.y + other.y)
        return p

    def __str__(self):
        return f"Point {self.x}, {self.y}"

p0 = Point(x=0, y=0)
p1 = Point(x=2, y=3)
p2 = Point(x=4, y=6)

#1
rasstoyanie = p1 + p0
print(rasstoyanie)

#2
p_two = p1 + p2
print(p_two)