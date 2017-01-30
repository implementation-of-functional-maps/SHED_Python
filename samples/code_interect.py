import code

for i in range(1, 10):
    print(i)
    if i == 5:
        print()
        code.interact("Mini DEbugger - use Ctrl-D to exit", None, locals())
        
