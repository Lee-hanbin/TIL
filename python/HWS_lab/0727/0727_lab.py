# 7_2

class Doggy():
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self, name, breed ):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.burth_of_dogs += 1
    
    def bark():
        print('월월')
    
    @classmethod
    def get_status()
