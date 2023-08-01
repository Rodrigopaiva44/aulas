def f(v):
    print(v)


def dumb():
    return f


var = dumb()
var("pode imprimir")


def dumb2():
    return "dois", "valores"


var2 = dumb2()
print(var2, type(var2))
