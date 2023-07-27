def test(a1, a2, a3, nome=None, a4=None):
    print(a1, a2, a3, nome, a4)
    return nome, a4  # sem return a var é none


test(1, 2, 3, nome="Rodrigo", a4="4")
var = test(1, 2, 3, "Rodrigo", "4")
print(var)
print(var[0], var[1])

# E quando eu não sei quantos argumentos?


def test(*args):
    print(args)


lista = [1, 2, 3, 4, 5]

# Desempacotando n1 e n2 e empacotando o restante
n1, n2, *n = lista
print(n1, n2, n)
# Desempacotando a lista
print(*lista)


def test(*args):
    print(args)
    args = list(args)
    args[0] = 99
    print(args)


test(1, 2, 3, 4, 5)
