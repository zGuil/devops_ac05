import pytest
from com.mongoloides.converte_hora import converteHora

def test_convertehora():
	assert converteHora(1,45) == '01:45 AM'
