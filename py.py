class Plantacao:
    def __init__(self, cultura, area_hectares, produtividade_estim):
        self.cultura = cultura
        self.area_hectares = area_hectares
        self.produtividade_estim = produtividade_estim  # sacas por hectare

    def estimativa_colheita(self):
        return self.area_hectares * self.produtividade_estim

    def __str__(self):
        return (f"Cultura: {self.cultura}\m"
                f"Área: {self.area_hectares} km2\m"
                f"Produtividade Estimada: {self.produtividade_estim} sacas/saco\m"
                f"Total Estimado: {self.estimativa_colheita()} sacas\n")


# Cadastro de plantações
plantacoes = []

# Exemplo de uso
plantacoes.append(Plantacao("Soja", 50, 60))
plantacoes.append(Plantacao("Milho", 30, 80))

# Exibir relatório
for p in plantacoes:
    print(p)
