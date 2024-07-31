# Dicionário inicial de alunos
alunos = {
    "Alice": 24,
    "Bob": 22,
    "Charlie": 23
}

while True:
    # Menu de opções
    print("\nMenu:")
    print("1. Listar alunos")
    print("2. Adicionar aluno")
    print("3. Remover aluno")
    print("4. Atualizar idade do aluno")
    print("5. Sair")
    
    escolha = int(input("Escolha uma opção: "))
    
    if escolha == 1:
        # Listar alunos
        for nome, idade in alunos.items():
            print(f"{nome} tem {idade} anos.")
    
    elif escolha == 2:
        # Adicionar aluno
        nome = input("Digite o nome do aluno: ")
        idade = int(input(f"Digite a idade de {nome}: "))
        alunos[nome] = idade
        print(f"Aluno {nome} adicionado.")
    
    elif escolha == 3:
        # Remover aluno
        nome = input("Digite o nome do aluno a ser removido: ")
        if nome in alunos:
            del alunos[nome]
            print(f"Aluno {nome} removido.")
        else:
            print(f"Aluno {nome} não encontrado.")
    
    elif escolha == 4:
        # Atualizar idade do aluno
        nome = input("Digite o nome do aluno cuja idade deseja atualizar: ")
        if nome in alunos:
            idade = int(input(f"Digite a nova idade de {nome}: "))
            alunos[nome] = idade
            print(f"Idade de {nome} atualizada para {idade} anos.")
        else:
            print(f"Aluno {nome} não encontrado.")
    
    elif escolha == 5:
        # Sair
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
