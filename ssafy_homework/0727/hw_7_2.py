class Doggy:
    birth_of_dogs = 0
    num_of_dogs = 0
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Doggy.birth_of_dogs += 1
        Doggy.num_of_dogs += 1

    def bark(self):
        print(f'{self.name}가 짖는다.')
    
    def __del__(self):
        Doggy.num_of_dogs -= 1
        print(f'{self.name}가 무지개다리를 건넜습니다.')
    
    @classmethod
    def get_status(cls):
        print(cls.birth_of_dogs, cls.num_of_dogs)


d1 = Doggy('뭉치', '스피치')
d2 = Doggy('왕눈이', '치와와')
d3 = Doggy('까미', '리트리버')

Doggy.get_status()

d1.bark()
d2.bark()
d3.bark()
del d3
Doggy.get_status()