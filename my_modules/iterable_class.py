from __future__ import print_function
import weakref

class IterableCar(type):

    _cars = weakref.WeakSet()

    def __iter__(cls):
        return iter(cls._cars)

    def add_car(cls, car):
        return cls._cars.add(car)


class Car(metaclass=IterableCar):

    def __init__(self, name):
        self.__class__.add_car(self)
        self.name = name


if __name__=='__main__':

    car1 = Car('Mercedes')
    car2 = Car('Toyota')
    for cars in Car:
        print (cars.name)
