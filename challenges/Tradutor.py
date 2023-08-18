# Crie um tradutor que substitua todas as vogais por G


def tradutor(frase):
    traducao = ''
    for letra in frase:
        if letra in 'AEIOUaeiou':
            traducao = traducao + 'g'
        else:
            traducao = traducao + letra
    return traducao


print(tradutor(input("diga uma frase: ")))
