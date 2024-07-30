# Dicionário inicial

# Atualize o valor associado a uma chave específica no dicionário
idades = {
    "Ana": 25,
    "Bruno": 30,
    "Carla": 22,
    "Daniel": 35
}

# Atualize a idade de "Daniel"
idades["Daniel"] = 36

# Imprima o dicionário atualizado
print(idades)

# Agora Atualize o valor associado a uma chave escolhida pelo usuário

idades = {
    "Ana": 25,
    "Bruno": 30,
    "Carla": 22,
    "Daniel": 35
}

# Solicite ao usuário o nome da pessoa cuja idade deseja atualizar
nome = input("Digite o nome da pessoa cuja idade deseja atualizar: ")

# Verifique se o nome está no dicionário
if nome in idades:
    # Solicite ao usuário a nova idade
    nova_idade = int(input(f"Digite a nova idade de {nome}: "))
    # Atualize a idade no dicionário
    idades[nome] = nova_idade
    # Imprima o dicionário atualizado
    print(f"Idade de {nome} atualizada com sucesso.")
else:
    print(f"{nome} não está no dicionário.")

# Imprima o dicionário atualizado
print(idades)


# Itere sobre o dicionário e imprima chaves e valores
idades = {
    "Ana": 25,
    "Bruno": 30,
    "Carla": 22,
    "Daniel": 35
}
for nome, idade in idades.items():
    print(f"{nome} tem {idade} anos")



# Crie um dicionário vazio
idades = {}

# Permita ao usuário adicionar três pares chave-valor
for i in range(3):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    idades[nome] = idade

# Imprima o dicionário atualizado
print("Dicionário após adições:", idades)
