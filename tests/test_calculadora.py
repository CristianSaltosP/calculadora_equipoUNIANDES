import pytest
from src.calculadora import mediana, desviacion_estandar

def test_mediana_lista_impar():
    assert mediana([1, 3, 5]) == 3

def test_mediana_lista_par():
    assert mediana([1, 2, 3, 4]) == 2.5

def test_desviacion_estandar():
    resultado = desviacion_estandar([1, 2, 3, 4, 5])
    assert round(resultado, 2) == 1.41

def test_lista_vacia_mediana():
    with pytest.raises(ValueError):
        mediana([])

def test_lista_vacia_desviacion():
    with pytest.raises(ValueError):
        desviacion_estandar([])
