# 실습 8_2

from datetime import datetime

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age - 1

    @classmethod
    def details(cls, name, year):
        age =  datetime.today().year - year
        cls.name = name
        return cls(name ,age)

    def check_age(self):
        print(self.name,'의 나이는 만' ,self.age, '입니다.')
        if self.age < 19:
            return False
        else:
            return True
p1 = Person('hb', 20)
print(p1.name, p1.age)
p2 = Person.details('mh', 1997)
print(p2)
print(p2.check_age())
print(p1.check_age())
