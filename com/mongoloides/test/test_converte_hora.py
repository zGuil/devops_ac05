import pytest
from com.mongoloides.converte_hora import converteHora

def test_convertehora():
	converte = converte_hora()
	assert converte.converteHora(1,45) == '01:45 AM'