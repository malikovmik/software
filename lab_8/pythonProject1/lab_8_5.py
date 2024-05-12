class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Car is driving"


class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is riding"


def race(vehicles):
    for vehicle in vehicles:
        print(vehicle.move())


car = Car()
bicycle = Bicycle()

race([car, bicycle])
