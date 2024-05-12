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
        print(f'Привет, меня зовут {self._name}, мне уже {self._age} лет')

class Cat(Animal):
    def __init__(self, poroda, age, name, color):
        super().__init__(age, name, color)
        self.poroda =poroda

    def make_sound(self):
        print("meaw")

my_cat = Cat("sphinx", 9, "Shao", "Grey")

print(my_cat._name)
print(my_cat._age)
my_cat.sleep()
my_cat.hello()

class Dog(Animal):
    def __init__(self, poroda, age, name, color):
        super().__init__(age, name, color)
        self.__poroda = poroda

    def make_sound(self):
        print("Woof")

my_dog = Dog("dog", 7, 'Wolf', 'White')

print(my_dog._name)
my_dog.sleep()
my_dog.hello()
print(f'Мой цвет {my_dog.__color}')
