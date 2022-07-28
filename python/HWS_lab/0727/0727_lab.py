# 7_2

class Doggy():
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self, name, breed ):
        self.name = name
        self.breed = breed
        print(f'{breed}종인 {name}가 태어났습니다.')
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
    
    def die(self):
        print('사망')
        Doggy.num_of_dogs -= 1

    def bark(self):
        print('월월')
    
    @classmethod
    def get_status(cls):
        print(f'태어난 개의 수 : {cls.birth_of_dogs}, 현재 있는 개의 수 : {cls.num_of_dogs}')


Doggy1 = Doggy('멍멍','말티즈')
Doggy1.bark()
Doggy2 = Doggy('멍멍멍','푸들')
Doggy2.bark()
Doggy3 = Doggy('멍', '치와와')
Doggy3.bark()
Doggy.get_status()
Doggy3.bark()
Doggy3.die()
Doggy.get_status()
