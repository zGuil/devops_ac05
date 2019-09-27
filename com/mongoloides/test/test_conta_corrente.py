import pytest
from com.mongoloides.conta_corrente import ContaCorrente


def test_alterarNome():
    conta = ContaCorrente(1802, "Wesley", saldo=10)
    assert conta.alterarNome("Guilherme") == conta.nomeCorrentista
    assert conta.deposito(300) == conta.saldo
    assert conta.saque(300) == conta.saldo
