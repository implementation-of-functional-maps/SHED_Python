from __future__ import print_function
import weakref
from itertools import chain, repeat

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

def Struct(name, *fields):
  
  def __init__(self, *args):
    if len(args) > len(fields):
      raise TypeError("__init__() takes at most %d arguments (%d given)" % (len(fields)+1, len(args)+1))
    args = chain(args, repeat(None))
    for field, value in zip(fields, args):
      setattr(self, field, value)
    
  attrs = dict()
  # attrs["__slots__"] = fields
  attrs["__init__"] = __init__
  return type(name, (object,), attrs)


if __name__=='__main__':
    Foo = Struct("Foo", "foo", "bar")
    f = Foo([1,1,], 2)
    f = Foo([3,2], 4)
    
    car1 = Car(f.foo)
    car2 = Car(f.bar)
    
    for cars in Car:
        print (cars.name)
