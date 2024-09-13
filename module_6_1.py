class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = Plant.name
        if edible = True:
            print(f'{self.name} съел {food.name}')
            fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            alive = False


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
