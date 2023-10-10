import argparse


def processar_escolha(opcao, mensagem):
    if opcao == 'A':
        resultado = len(mensagem)
    elif opcao == 'B':
        resultado = mensagem.count(' ')
    elif opcao == 'C':
        resultado = sum(map(int, mensagem.split()))
    else:
        print("Opção inválida. Escolha entre A, B ou C.")
        return

    print(f"Opção {opcao} selecionada. Resultado: {resultado}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Processa uma escolha e mensagem personalizada.")
    parser.add_argument(
        "--opcao", choices=['A', 'B', 'C'], required=True, help="Escolha entre A, B ou C.")
    parser.add_argument(
        "--mensagem", help="Mensagem personalizada para processamento.")

    args = parser.parse_args()

    opcao = args.opcao
    mensagem = args.mensagem

    processar_escolha(opcao, mensagem)
