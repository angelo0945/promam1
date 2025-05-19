import random

def jogar_forca():
    palavras = ["código", "onichan", "arigato", "ornitorinco"]
    palavra = random.choice(palavras)
    letras_corretas = ["_"] * len(palavra)
    tentativas = 6
    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca!")

    while tentativas > 0 and "_" in letras_corretas:
        print("Palavra:", " ".join(letras_corretas))
        print("Tentativas restantes:", tentativas)
        print("Letras erradas:", letras_erradas)
        letra = input("Digite uma letra: ").lower()

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letras_corretas[i] = letra
        else:
            tentativas -= 1
            letras_erradas.append(letra)

    if "_" not in letras_corretas:
        print("Você ganhou! A palavra era:", palavra)
    else:
        print("Você perdeu! A palavra era:", palavra)

jogar_forca()