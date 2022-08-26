import pytest
import numpy as np
from matematica.Calculadora import soma, sub, multiplicacao, divisao, media_lista_valores

@pytest.mark.op_simples
def test_soma():
    assert soma(1, 2) == 3

def test_sub():
    assert sub(1, 2) == -1

def test_multiplicacao():
    assert multiplicacao(1, 2) == 2

def test_divisao():
    assert divisao(1, 2) == 0.5

def test_media_lista_valores():
    assert media_lista_valores([1, 2, 3, 4, 5]) == 3.0

# --------------- Exercício 1 -----------------
@pytest.mark.ex1
def test_divisao_por_zero():
    assert divisao(1, 0) == np.inf

@pytest.mark.ex1
def test_media_lista_vazia():
    assert media_lista_valores([]) == 0

@pytest.mark.ex1
def test_media_lista_com_strings():
    assert media_lista_valores([2, 4, "Insper", 6, 0]) == 3.0



    
    

