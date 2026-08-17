"""
Calculadora básica para práctica de GCS.
Versión: v1.0.0
"""
import math

def mediana(valores):
    """Calcula la mediana de una lista de números."""
    n = len(valores)
    if n == 0:
        raise ValueError("La lista está vacía")
    valores_ordenados = sorted(valores)
    mitad = n // 2
    if n % 2 == 0:
        return (valores_ordenados[mitad - 1] + valores_ordenados[mitad]) / 2
    else:
        return valores_ordenados[mitad]

def desviacion_estandar(valores):
    """Calcula la desviación estándar de una lista de números."""
    n = len(valores)
    if n == 0:
        raise ValueError("La lista está vacía")
    media = sum(valores) / n
    varianza = sum((x - media) ** 2 for x in valores) / n
    return math.sqrt(varianza)


# TODO (CR-1): implementar mediana(valores) y desviacion_estandar(valores)
