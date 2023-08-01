def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [1, 2, 3, 4, 5]
print(f'Os valores são {valores}')
dobra(valores)
print(valores)


# Somando numeros
def soma(* valor):
    s = 0
    for num in valor:
        s += num
    print(f'Somando os valores {valor} temos {s}')


soma(5, 2)
soma(3, 2)
