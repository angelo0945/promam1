import random
import time

class SensorUmidade:
    def ler_umidade(self):
        # Simula a leitura da umidade do solo (0 a 100%)
        return random.randint(20, 100)

class SistemaIrrigacao:
    def __init__(self, limite_umidade):
        self.limite_umidade = limite_umidade
        self.ativo = False

    def verificar_e_acionar(self, umidade):
        if umidade < self.limite_umidade:
            self.ativo = True
            print(f"Umidade baixa ({umidade}%). Irrigação ativada.")
        else:
            self.ativo = False
            print(f"Umidade adequada ({umidade}%). Irrigação desligada.")

# Simulação do sistema
sensor = SensorUmidade()
sistema = SistemaIrrigacao(limite_umidade=100)

# Executar leitura por 5 ciclos
for _ in range(5):
    umidade = sensor.ler_umidade()
    sistema.verificar_e_acionar(umidade)
    time.sleep(1)  # Pausa de 1 segundo (simula passagem de tempo)

