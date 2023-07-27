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
print(*lista, sep=", ")


def test(*args):
    print(args)
    args = list(args)  # Fazendo um cast de T -> L
    args[0] = 99
    print(args)


test(1, 2, 3, 4, 5)


def test(*args):
    print(args)


lista = [1, 2, 3]
test(lista, "4")
# Desempacotando a lista
test(*lista)

# Key Words arguments


def test(*args, **kwargs):
    print(args)
    print(kwargs["nome"], kwargs["sobrenome"])


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
test(*lista, *lista2, nome="Rodrigo", sobrenome="Paiva")


def test(*args, **kwargs):
    print(args)
    print(kwargs["nome"], kwargs["sobrenome"])

    idade = kwargs.get("idade")
    if idade is not None:
        print(idade)
    else:
        print("Não existe")


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
test(*lista, *lista2, nome="Rodrigo", sobrenome="Paiva")
