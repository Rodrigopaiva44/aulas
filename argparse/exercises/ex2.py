import argparse


def exibir_informacoes(idade, cidade):
    if idade:
        print(f"Idade: {idade}")
    if cidade:
        print(f"Cidade: {cidade}")
    if not idade and not cidade:
        print("Nenhuma informação fornecida.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Exibe informações opcionais.")
    parser.add_argument("--idade", type=int, help="Idade a ser exibida.")
    parser.add_argument("--cidade", help="Cidade a ser exibida.")

    args = parser.parse_args()
    idade = args.idade
    cidade = args.cidade

    exibir_informacoes(idade, cidade)
