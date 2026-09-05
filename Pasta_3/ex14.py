class CarteiraDigital:
    def __init__(self, nome_titular, saldo_inicial):
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial
    
    def transferir_pix(self, valor, carteira_destino):
        if valor <= self.saldo:
            self.saldo -= valor
            carteira_destino.saldo += valor
            print(f"Transferência de R${valor:.2f} realizada para {carteira_destino.nome_titular}. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para a transferência.")

cliente_a = CarteiraDigital("Kazu", 500.0)
cliente_b = CarteiraDigital("Maria", 100.0)

cliente_a .transferir_pix(150.0, cliente_b)
print(cliente_a.saldo)
print(cliente_b.saldo)