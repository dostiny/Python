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
        print(f'{self.name}는 하늘나라로~')
    
    @classmethod
    def get_status(cls):
        print(cls.birth_of_dogs, cls.num_of_dogs)


d1 = Doggy('갈비', '비글')
d2 = Doggy('윤이클로', '치와와')
d3 = Doggy('나쁜개', '모름')

Doggy.get_status()
del d3 # 메모리를 죽이는 시점에 바로 실행
Doggy.get_status()
d1.bark()
d2.bark()
