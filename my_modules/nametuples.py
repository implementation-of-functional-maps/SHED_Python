from collections import namedtuple
Foo = namedtuple("Foo", "foo bar")
f = Foo(1, 2)
print(f.foo)# 1
print(f.bar) # 2
