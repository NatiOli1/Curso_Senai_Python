from cliente import Cliente


class Conta:
    def __init__(self, nome, descricao,
                 cliente: Cliente, saldo=0.0):
        self.nome = nome
        self.descricao = descricao
        self.saldo = saldo
        self.cliente = cliente
        self.movimentacoes = []
        self.movimentacoes.append("Saldo inicial " + str(saldo))

    def depositar(self, valor):
        self.saldo += valor
        self.movimentacoes.append("Depositou " + str(valor))

    def sacar(self, valor):
        self.saldo -= valor
        self.movimentacoes.append("Sacou " + str(valor))


    def get_saldo(self):
        return self.saldo

    def get_extrato(self):
        for movimentacao in self.movimentacoes:
            print(movimentacao)
