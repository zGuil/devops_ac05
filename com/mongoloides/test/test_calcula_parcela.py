import pytest
from com.mongoloides.calcula_parcela import valorPagamento


def test_calcula():
    #calcula = calcula_parcela()
    assert valorPagamento(0, 2) == 0
