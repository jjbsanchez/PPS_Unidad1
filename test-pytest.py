__author__ = 'Juan José Burgos Sánchez'
__email__ = 'juanjose.burgos.fp@iescampanillas.com'

# Test con Pytest (versión usada: pytest 6.2.5)
# Asegurarse de tener instalado Pytest antes en la máquina a ejecutar el test
# Para instalar: pip3 install pytest si se está usando Python 3

# ejecutar test con el comando pytest test-pytest.py

import pytest

from binario import esBinario, convierteABinario
from lista import estaEnLista, estaEnRango


def test_esBinario():
    """Test para la función esBinario, que comprueba si el string pasado por parámetro está compuesto por números binarios
    """

    # Si introduce un string de números binarios correcto, devuelve True
    assert esBinario('1001') == True

    # Si introduce un string de números enteros que no son binarios, devuelve False
    assert esBinario('10012') == False

    # Si introduce un string alfanumérico, devuelve False
    assert esBinario('10012asf') == False

    # Si no introduce ningún parámetro, lanza un error
    with pytest.raises(ValueError, match=r".* valor .*"):
        esBinario()


def test_convierteABinario():
    """Test para la función convierteABinario, que convierte el string de números binarios pasado por parámetro a número decimal
    """

    # Si el string es un número binario correcto, devuelve la conversión a número decimal
    assert convierteABinario('1001') == 9

    # Si el string es alfanumérico, lanza un error
    with pytest.raises(ValueError, match=r".* valor .*"):
        convierteABinario('234fd')

    # Si no se pasa ningún parámetro, lanza un error
    with pytest.raises(ValueError, match=r".* valor .*"):
        convierteABinario()


def test_estaEnLista():
    """Test para la función estaEnLista, que comprueba si un número está dentro de una lista
    """

    # Lista de prueba para realizar el test
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Si el número está dentro de la lista, devuelve True
    assert estaEnLista(1, lista) == True

    # Si el número no está dentro de la lista, devuelve False
    assert estaEnLista(12, lista) == False

    # Si sólo se pasa un parámetro, lanza un error informando de que falta pasar una lista como parámetro
    with pytest.raises(ValueError, match=r".* lista.*"):
        estaEnLista(13)

    # Si no pasa ningún parámetro, lanza un error informando de que no ha introducido ningún parámetro
    with pytest.raises(ValueError, match=r".* parámetro.*"):
        estaEnLista()


def test_estaEnRango():
    """Test para la función estaEnRango, que comprueba si un número se encuentra dentro de un rango
    """

    # Si el número se encuentra dentro del rango proporcionado, devuelve True, (2 está entre el 1 y 5)
    assert estaEnRango(2, 1, 5) == True

    # Si el número no se encuentra dentro del rango proporcionado, devuelve False (9 no está entre 1 y 5)
    assert estaEnRango(9, 1, 5) == False

    # Si sólo se pasan 2 parámetros, lanza un error
    with pytest.raises(ValueError, match=r".* error.*"):
        estaEnLista(13, 12)

    # Si sólo se pasa un parámetro, lanza un error
    with pytest.raises(ValueError, match=r".* lista.*"):
        estaEnLista(13)

    # Si no se pasan parámetros, lanza un error
    with pytest.raises(ValueError, match=r".* valor.*"):
        estaEnRango()
