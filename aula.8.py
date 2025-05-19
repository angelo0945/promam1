def cadastrar_cliente():
    nome = input("nome: ")
    email = input("e-mail: ")
    senha = input("senha: ")

    try:
        idade = int(input("idade: "))
    except ValueError:
        print("Erro: a idade deve ser um número inteiro.")
        return

    if idade >= 25:
        print("\nCliente cadastrado com sucesso!")
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        print(f"E-mail: {email}")
        print(f"senha: {senha}")
        # Aqui você pode adicionar o cliente a uma lista ou salvar em um arquivo.
    else:
        print(f"\nCadastro negado. Cliente '{nome}' tem {idade} anos e precisa ter 25 anos ou mais.")

# Executar o cadastro
cadastrar_cliente()
