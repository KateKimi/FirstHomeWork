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
        return self.salary * money

e1 = Employee(full_name="Vasya Man", salary=100, age_birth=1987, experience=2, position='programmer')
print(e1.full_name)
print(e1.mon_position())
print(e1.mon_salary(2))
