__author__ = 'Juan José Burgos Sánchez'
__version__ = '1.0'
__email__ = 'juanjose.burgos.fp@iescampanillas.com'

"""Realiza, utilizando Python 3, un programa llamado binario.py que pida al usuario que introduzca un número binario e imprima por pantalla el número en formato decimal.
"""


def esBinario(strbinario=''):
    """devuelve True o False si la cadena de caracteres (strbinario) que se ha pasado como parámetro contiene una cadena binaria
        
    Parameters:
        strbinario (string): cadena de caracteres
    
    Raises:
        ValueError: El valor introducido no es válido
        
    Returns:
        bool: True si la cadena está compuesta por números binarios o False en caso contrario
        
    """

    if strbinario:

        esBin = False
        for character in strbinario:
            if character == '1' or character == '0':
                esBin = True
            else:
                esBin = False
                break
        return esBin

    else:
        raise ValueError("El valor introducido no es válido")


def convierteABinario(binario=''):
    """recibe un string de números binarios y lo devuelve convertido en decimal
        
    Parameters:
        binario (string): cadena de caracteres compuesta por números binarios
    
    Raises:
        ValueError: El valor introducido no es correcto
        
    Returns:
        int: binario convertido a decimal
        
    """

    # comprueba si la variable introducida por el usuario es un número binario, si es correcto, lo convierte, si no lanza un error
    if esBinario(binario):

        # suma total de decimales
        suma = 0

        # variable que usamos para asignar a cada binario su correspondiente conversión en decimal, irá aumentado multiplicado por 2 en cada iteración
        equivalente = 1

        # iteramos en la cadena de forma inversa
        for number in binario[::-1]:
            # si el binario es 1, añadimos a la suma total su correspondiente conversión en decimal
            if int(number) == 1:
                suma += equivalente
            equivalente *= 2
        return suma

    else:
        raise ValueError("El valor introducido no es correcto")


if __name__ == '__main__':

    # almacena el valor introducido por el usuario
    input_usuario = input("Introduce un número en binario: ")

    if convierteABinario(input_usuario):
        print(convierteABinario(input_usuario))