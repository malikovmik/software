class Animal:
    def __init__(self, age, name, color):
        self._age = age
        self.__color = color
        self._name = name

    def sleep(self):
        print("i am sleep,zzz")

    def eat(self):
        print("I am eating")

    def hello(self):
        print(f'Привет, меня зовут {self.name}, мне уже {self.age} лет')

class Cat(Animal):
    def __init__(self, poroda, age, name, color):
        super().__init__(age, name, color)
        self.poroda =poroda

    def make_sound(self):
        print("meaw")

my_cat = Cat("sphinx", 9, "Shao", "Grey")

print(my_cat.name)
my_cat.sleep()
my_cat.hello()