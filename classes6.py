class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self,valor):
        self.saldo = valor
        print(f"Valor depositado: {valor}")

    def sacar(self,valor):
        if self.saldo > valor:
            self.saldo = self.saldo - valor
            print(f"Valor sacado: {valor}\nSeu saldo: {self.saldo}")
        else:
            print("Sem Saldo!")
    
    def exibir_saldo(self):
        return self.saldo
    
conta_nubank = ContaBancaria()

# Depositando
conta_nubank.depositar(1000)
conta_nubank.exibir_saldo() # Exibindo o saldo

# Sacando
conta_nubank.sacar(500)
conta_nubank.exibir_saldo() # Exibindo o saldo