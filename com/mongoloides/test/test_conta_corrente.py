import pytest
from com.mongoloides.conta_corrente import ContaCorrente


def test_ContaCorrente():
    conta = ContaCorrente(4, "guilherme", 0)
    assert conta.alterarNome("Lucas") == conta.nomeCorrentista
    assert conta.deposito(300) == 300
    assert conta.saque(300) == 0
