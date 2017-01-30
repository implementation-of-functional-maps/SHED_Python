def _(f):
    print("f.Segments =", f.Segments)
    print("f.Vertices =", f.Vertices)
    print("length of f.Segments =", len(f.Segments))
    f.good = 3
    print("f.good =", f.good)    
    return None


# Foo = slot_class.Struct("Foo", "foo", "bar")
# f = Foo(1, 2)
