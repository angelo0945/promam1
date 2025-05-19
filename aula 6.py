import random

def jogar_pedra_papel_tesoura():
    escolhas = ["pedra", "papel", "tesoura"]
    escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()
    escolha_computador = random.choice(escolhas)

    print(f"Você escolheu: {escolha_usuario}")
    print(f"O computador escolheu: {escolha_computador}")

    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
         (escolha_usuario == "papel" and escolha_computador == "pedra") or \
         (escolha_usuario == "tesoura" and escolha_computador == "papel"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

jogar_pedra_papel_tesoura()