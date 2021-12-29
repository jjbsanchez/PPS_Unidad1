__author__ = 'Juan José Burgos Sánchez'
__email__ = 'juanjose.burgos.fp@iescampanillas.com'

import unittest
from binario import esBinario, convierteABinario
from lista import estaEnLista, estaEnRango


class Tests(unittest.TestCase):

    def test_esBinario(self):
        """Test para la función esBinario, que comprueba si el string pasado por parámetro está compuesto por números binarios
        """

        # Si introduce un string de números binarios correcto, devuelve True
        self.assertEqual(esBinario('1001'), True)

        # Si introduce un string de números enteros que no son binarios, devuelve False
        self.assertEqual(esBinario('1021'), False)

        # Si introduce un string alfanumérico, devuelve False
        self.assertEqual(esBinario('3249fsd'), False)

        # Si no introduce ningún parámetro, lanza un error
        self.assertRaises(ValueError, esBinario)

    def test_convierteABinario(self):
        """Test para la función convierteABinario, que convierte el string de números binarios pasado por parámetro a número decimal
        """

        # Si el string es un número binario correcto, devuelve la conversión a número decimal
        self.assertEqual(convierteABinario('1001'), 9)

        # Si el string son números que no son binarios, lanza un Error
        self.assertRaises(ValueError, convierteABinario, '10234')

        # Si el string es alfanumérico, lanza un Error
        self.assertRaises(ValueError, convierteABinario, '10234dsf')

        # Si no se pasa ningún parámetro, lanza un error
        self.assertRaises(ValueError, convierteABinario)

    def test_estaEnLista(self):
        """Test para la función estaEnLista, que comprueba si un número está dentro de una lista
        """

        # Lista de prueba para realizar el test
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Si el número está dentro de la lista, devuelve True
        self.assertEqual(estaEnLista(1, lista), True)

        # Si el número no está dentro de la lista, devuelve False
        self.assertEqual(estaEnLista(12, lista), False)

        # Si no pasa ningún parámetro, lanza un error informando de que no ha introducido ningún parámetro
        self.assertRaises(ValueError, estaEnLista)

        # Si pasa un valor incorrecto por parámetro, lanza un error informando de que el valor no es correcto
        self.assertRaises(ValueError, estaEnLista, '13')

        # Si sólo se pasa un parámetro, lanza un error informando de que falta pasar una lista como parámetro
        self.assertRaises(ValueError, estaEnLista, 13)

    def test_estaEnRango(self):
        """Test para la función estaEnRango, que comprueba si un número se encuentra dentro de un rango
        """

        # Si el número se encuentra dentro del rango proporcionado, devuelve True, (2 está entre el 1 y 5)
        self.assertEqual(estaEnRango(2, 1, 5), True)

        # Si el número no se encuentra dentro del rango proporcionado, devuelve False (7 no está entre 1 y 5)
        self.assertEqual(estaEnRango(7, 1, 5), False)

        # Si algunos de los valores son incorrectos, lanza un error
        self.assertRaises(ValueError, estaEnRango, 2, 3, 'a')

        # Si todos los valores son incorrectos, lanza un error
        self.assertRaises(ValueError, estaEnRango, '1', 'b', '3')

        # Si no se pasan valores por parámetros, lanza un error
        self.assertRaises(ValueError, estaEnRango)


if __name__ == '__main__':
    unittest.main()