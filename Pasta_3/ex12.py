# A classe de ar-condicionado representa um dispositivo que pode ser ligado, desligado e ajustar a temperatura.
class ArCondicionado:
    # Construtor da classe ArCondicionado que inicializa a temperatura.
    def __init__(self, temperatura):
        self.temperatura = temperatura

    # Método ligar = Método que liga o ar-condicionado e exibe a temperatura atual.
    def ligar(self):
        print(f"Ar-condicionado ligado a {self.temperatura}°C.")
    
    # Método desligar = Método que desliga o ar-condicionado.
    def desligar(self):
        print("Ar-condicionado desligado.")

    # Método aumentar_temperatura = Método que aumenta a temperatura do ar-condicionado em um valor especificado.
    def aumentar_temperatura(self, incremento):
        self.temperatura += incremento
        print(f"Temperatura aumentada para {self.temperatura}°C.")

    # Método diminuir_temperatura = Método que diminui a temperatura do ar-condicionado em um valor especificado.
    def diminuir_temperatura(self, decremento):
        self.temperatura -= decremento
        print(f"Temperatura diminuída para {self.temperatura}°C.")

# Exemplo de uso da classe ArCondicionado
print("Bem-vindo ao controle do ar-condicionado!")

# Cria um objeto da classe ArCondicionado com temperatura inicial de 20°C
meu_ar = ArCondicionado(20)

# Liga o ar-condicionado, aumenta a temperatura em 5°C, diminui em 3°C e desliga o ar-condicionado
meu_ar.ligar()
meu_ar.aumentar_temperatura(5)
meu_ar.diminuir_temperatura(3)
meu_ar.desligar()