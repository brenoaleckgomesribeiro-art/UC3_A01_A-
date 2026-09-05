class ArCondicionado:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    def ligar(self):
        print(f"Ar-condicionado ligado a {self.temperatura}°C.")

    def desligar(self):
        print("Ar-condicionado desligado.")

    def aumentar_temperatura(self, incremento):
        self.temperatura += incremento
        print(f"Temperatura aumentada para {self.temperatura}°C.")

    def diminuir_temperatura(self, decremento):
        self.temperatura -= decremento
        print(f"Temperatura diminuída para {self.temperatura}°C.")

print("Bem-vindo ao controle do ar-condicionado!")

meu_ar = ArCondicionado(20)

meu_ar.ligar()
meu_ar.aumentar_temperatura(5)
meu_ar.diminuir_temperatura(3)
meu_ar.desligar()