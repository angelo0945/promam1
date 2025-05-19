class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")

# Criando objetos
produto1 = Produto("Caneta", 2.50)
produto2 = Produto("Caderno grande", 80.00)

# Exibindo os produtos
produto1.exibir()
produto2.exibir()
 