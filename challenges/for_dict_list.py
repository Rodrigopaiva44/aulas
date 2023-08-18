# Escreva um programa que capture dados sobre três estados do Brasil:
# a Unidade Federativa (UF) e a sigla do estado. Você vai usar um dicionário
# chamado 'estado' para armazenar essas informações e, em seguida, adicionar
# cada dicionário à lista 'brasil'. Ao final, o programa deverá exibir
# todos os dados coletados.


estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado'))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.items():
        print(v, end=' ')
