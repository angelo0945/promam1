class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir(self):
        print(f"{self.nome} - R${self.preco:.2f} - {self.quantidade} unidades")

# Criando produtos
produto1 = Produto("computador gamer", 11445, 1)
produto2 = Produto("iphone 16", 5585, 1)

# Exibindo os produtos
produto1.exibir()
produto2.exibir()
