import argparse


def saudacao(nome):
    print(f"Olá, {nome}!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Saudação personalizada.")
    parser.add_argument("--nome", required=True, help="Nome para a saudação.")

    args = parser.parse_args()
    nome = args.nome

    saudacao(nome)
