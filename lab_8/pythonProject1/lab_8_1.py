class Animal:
    def __init__(self, age, name, color):
        self.age = age
        self.name = name
        self.color = color

    def sleep(self):
        print("i am sleeping, zzz")

    def eat(self):
        print("I am eating")

    def hello(self):
        print(f'Привет, меня зовут {self.name}, мне уже {self.age} лет. Часто говорят, что у меня {self.color} цвет')

my_animal = Animal(9, 'Мурзик', 'серый')
my_animal.hello()

