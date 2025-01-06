class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.dinheiro = True

    def comprar(self):
        self.dinheiro = False
        return 'Você gastou seu dinheiro'

    def nao_comprar(self):
        self.dinheiro = True
        return 'Você Não gastou seu dinheiro'

cliente1 = Cliente('ivyson')

print(cliente1.dinheiro) # exibindo o dinheiro do cliente

print(cliente1.comprar()) # Gastando dinheiro ou não gastando (Alterar função para testes)

print(cliente1.dinheiro) # exibindo o dinheiro do cliente