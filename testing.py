def jogo():
    print("*"*50)
    print("Bem Vindo ao Jogo da Forca")
    print("*"*50)

    palavra_secreta = "careca"

    tentativa = ""
    erros = 0
    palavras_acertadas = []

    while tentativa != palavra_secreta or erros >= 3:
        tentativa = input("Tentativa: ").lower().strip()

        if tentativa == palavra_secreta:
            print("Você ganhou!")
            break
        else:
            for index, letra in enumerate(palavra_secreta):
                if letra in tentativa:
                    print(letra, sep="_", end=" ")
                    palavras_acertadas.insert(index, letra)
                else:
                    print("_", sep="_", end=" ")
        print()


if __name__ == "__main__":
    jogo()
