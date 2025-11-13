import pytest
from imc import *

def test_calculo_imc_valor_correto():
    # Teste se calcular_imc(70, 1.75) retorna 22.86
    assert calcular_imc(70, 1.75) == 22.86

def test_calculo_imc_arredondamento():
    # O IMC exato seria 22.857..., então deve arredondar para 22.86
    resultado = calcular_imc(70, 1.75)
    assert resultado == round(70 / (1.75 ** 2), 2)

def test_calculo_imc_altura_zero_erro():
    # Teste se passar altura = 0 gera ValueError
    with pytest.raises(ValueError):
        calcular_imc(70, 0)

def test_classificacao_abaixo_do_peso():
    assert classificar_imc(17.9) == "Abaixo do peso"

def test_classificacao_peso_normal():
    assert classificar_imc(22.0) == "Peso normal"

def test_classificacao_sobrepeso():
    assert classificar_imc(27.3) == "Sobrepeso"

def test_classificacao_obesidade_grau_I():
    assert classificar_imc(33.0) == "Obesidade grau I"

def test_classificacao_obesidade_grau_II():
    assert classificar_imc(37.0) == "Obesidade grau II"

def test_classificacao_obesidade_grau_III():
    assert classificar_imc(45.0) == "Obesidade grau III"
