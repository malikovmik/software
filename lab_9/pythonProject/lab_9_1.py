# Определение класса Tomato, представляющего отдельный помидор
class Tomato:
    # Словарь, содержащий стадии созревания помидора
    states = {
        1: 'отсутствует',
        2: 'цветение',
        3: 'зеленый',
        4: 'красный'
    }

    # Конструктор класса, инициализирующий помидор с заданным индексом
    def __init__(self, index):
        self._index = index  # Индекс помидора
        self._state = self.states[1]  # Начальная стадия помидора (цветение)

    # Метод, который делает помидор зрелее на одну стадию
    def grow(self):
        if self._state != self.states[len(self.states)]:  # Если помидор не достиг последней стадии созревания
            current_state_index = list(self.states.keys())[list(self.states.values()).index(self._state)]
            # Находим индекс текущей стадии созревания
            self._state = self.states[current_state_index + 1]  # Переводим помидор на следующую стадию

    # Метод, который проверяет, что помидор созрел
    def is_ripe(self):
        return self._state == self.states[len(self.states)]  # Возвращаем True, если помидор на последней стадии созревания


# Определение класса TomatoBush, представляющего куст с помидорами
class TomatoBash:
    # Конструктор класса, создающий заданное количество помидоров на кусте
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]  # Создаем список помидоров

    # Метод, который делает все помидоры на кусте зрелее на одну стадию
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()  # Вызываем метод grow() для каждого помидора на кусте

    # Метод, который проверяет, все ли помидоры на кусте созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])  # Проверяем созрели ли все помидоры на кусте

    # Метод, который собирает урожай, убирая с куста незрелые помидоры
    def give_away_all(self):
        self.tomatoes = [tomato for tomato in self.tomatoes if not tomato.is_ripe()]  # Оставляем только зрелые помидоры


# Определение класса Gardener, представляющего садовника
class Gardener:
    # Конструктор класса, инициализирующий садовника с заданным именем и кустом с помидорами
    def __init__(self, name, plant):
        self.name = name  # Имя садовника
        self._plant = plant  # Куст с помидорами

    # Метод, который заставляет садовника ухаживать за кустом с помидорами
    def work(self):
        self._plant.grow_all()  # Вызываем метод grow_all() для куста с помидорами

    # Метод, который проверяет, все ли помидоры на кусте созрели и собирает урожай при необходимости
    def harvest(self):
        if self._plant.all_are_ripe():  # Если все помидоры на кусте созрели
            print("Урожай собран!")
            self._plant.give_away_all()  # Собираем урожай
        else:
            print("Предупреждение: помидоры не созрели, продолжайте ухаживать")


    # Статический метод, предоставляющий справку по садоводству
    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("1. Регулярно поливайте растения")
        print("2. Удалите сорняки вокруг кустов")
        print("3. Подкармливайте удобрениями для лучшего роста и урожайности")


# Вывод справки по садоводству
Gardener.knowledge_base()

# Создание куста с помидорами и садовника
bush = TomatoBash(5)
gardener = Gardener("Пётр", bush)

# Уход за кустом с помидорами и сбор урожая
gardener.work()
gardener.harvest()

gardener.work()
gardener.work()
gardener.work()

gardener.harvest()
