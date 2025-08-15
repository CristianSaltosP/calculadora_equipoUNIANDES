"""
Calculadora básica para práctica de GCS.
Versión: v1.0.0
"""

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir para cero")
    return a / b

# TODO (CR-1): implementar mediana(valores) y desviacion_estandar(valores)
