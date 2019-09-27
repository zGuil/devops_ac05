class ContaCorrente:

    def __init__(self, numero, nomeCorrentista, saldo=0.0):
        self.numero = numero
        self.alterarNome(nomeCorrentista)
        self.saldo = saldo

    def alterarNome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista
        return self.nomeCorrentista

    def deposito(self, valor):
        self.saldo += valor
        return self.saldo

    def saque(self, valor):
        self.saldo -= valor
        return self.saldo
