class ContaBancaria():
    def __init__(self, valor_inicial ):
        self.saldo = valor_inicial
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            #self.saldo = self.saldo - valor
            self.saldo -= valor
            print(f"Valor sacado {valor}")
    def deposita(self, valor):
        self.saldo += valor
    def verificar_saldo(self):
        print(f"O saldo atual é de {self.saldo}")

contabancaria1 = ContaBancaria(40)
contabancaria1.verificar_saldo()
contabancaria1.deposita(30)
contabancaria1.sacar(100)
contabancaria1.sacar(10)
contabancaria1.verificar_saldo()