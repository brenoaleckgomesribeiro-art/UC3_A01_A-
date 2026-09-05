class ContaBancaria:
    def __init__(self, titular, saldo): 
        self.saldo = 0.0
        self.titular = titular

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para o saque.")
minha_conta = ContaBancaria("Kazu", 0.0)

minha_conta.depositar(100.0)
minha_conta.sacar(150.0)
minha_conta.sacar(50.0)