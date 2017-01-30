from itertools import chain, repeat


    
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

if __name__ == "__main__":
  Foo = Struct("Foo", "foo", "bar")
  f = Foo(1, 2)
  f = Foo(3, 4)
  
  print("f.foo =", f.foo)
  print("f.bar =", f.bar)
  f.foo = 0                     # OK
  # try:
  #   f.baz = 0                   # NG
  # except AttributeError, e:
  #   print(e)


  import slot_class_test
  import slot_class
  Shape = slot_class.Struct("Shape", "Segments", "Vertices")
  f = Shape([1, 2,3], [1,2,2])
  slot_class_test._(f)
