def jogar_caca_ao_tesouro():
    print("Você está em uma floresta. Escolha o caminho a seguir.")
    escolha = input("Digite 'esquerda' ou 'direita': ").lower()

    if escolha == "esquerda":
        print("Você encontrou um rio. Nade para o outro lado!")
        escolha2 = input("Digite 'nadar' para nadar ou 'voltar' para voltar: ").lower()
        if escolha2 == "nadar":
            print("Você chegou ao outro lado e encontrou o tesouro! Parabéns!")
        else:
            print("Você voltou e está perdido na floresta.")
    elif escolha == "direita":
        print("Você encontrou uma caverna escura. Enfrente o desafio!")
        escolha2 = input("Digite 'entrar' para entrar ou 'voltar' para voltar: ").lower()
        if escolha2 == "entrar":
            print("Você enfrentou um dragão e encontrou o tesouro!")
        else:
            print("Você voltou e se perdeu na floresta.")
    else:
        print("Escolha inválida. Jogo encerrado.")

jogar_caca_ao_tesouro()