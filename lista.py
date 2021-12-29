__author__ = 'Juan José Burgos Sánchez'
__version__ = '1.0'
__email__ = 'juanjose.burgos.fp@iescampanillas.com'

"""Crea un programa que reciba un número del 1 al 20 introducido por el usuario y compruebe si está
    dentro de la siguiente lista: [6,14,11,3,2,1,15,19]. Implementa una función que se asegure que el
    número introducido por el usuario está en el rango indicado y otra que compruebe si está dentro
    de la lista. Trata de crear las funciones de forma que puedan ser reutilizadas lo máximo posible en
    otros programas
"""

lista_a_comprobar = [6, 14, 11, 3, 2, 1, 15, 19]


def estaEnRango(valor='', minimo='', maximo=''):
    """devuelve True o False determinando qué valor se encuentra entre el mínimo y el máximo

    Args:
        valor (int): valor a comprobar
        minimo (int): valor mínimo de rango
        maximo (int): valor máximo de rango
        
    Raises:
        ValueError: Algunos de los parámetros introducidos tiene valores incorrectos
        ValueError: No has introducido un valor como parámetro
        ValueError: No has introducido un valor mínimo como parámetro
        ValueError: No has introducido un valor máximo como parámetro
        
    Returns:
        bool: True si el valor está en rango o en caso contrario False
        
    """

    # Si el usuario ha introducido todos los parámetros
    if valor != '' and minimo != '' and maximo != '':

        # Si los parámetros son números enteros, hace la comprobación
        if isinstance(valor, int) and isinstance(minimo, int) and isinstance(
                maximo, int):
            return valor >= minimo and valor <= maximo

        else:
            raise ValueError(
                "Algunos de los parámetros introducidos tiene valores incorrectos"
            )

    elif valor == '':
        raise ValueError("No has introducido un valor como parámetro")

    elif minimo == '':
        raise ValueError("No has introducido un valor mínimo como parámetro")

    elif maximo == '':
        raise ValueError("No has introducido un valor máximo como parámetro")


def estaEnLista(valor='', lista=[]):
    """devuelve True o False determinando si el valor está en la lista
    
    Args:
        valor (int): valor a comprobar si está en lista
        lista (list): lista a comprobar
        
    Raises:
        ValueError: Ha ocurrido un error con algunos de los parámetros que has introducido
        ValueError: No has introducido un valor
        ValueError: No has introducido una lista
        ValueError: No has introducido ningún parámetro
        
    Returns:
        bool: True si el valor está dentro de la lista o False en caso contrario  
    """

    if valor != '' and lista != []:

        if isinstance(valor, int):

            try:
                min_value = min(lista)
                max_value = max(lista)

                if estaEnRango(valor, min_value, max_value):

                    for number in lista:
                        if valor == number:
                            return True
                else:
                    return False

            except:
                raise ValueError(
                    "Ha ocurrido un error con algunos de los parámetros que has introducido."
                )

    elif valor == '' and lista != []:
        raise ValueError("No has introducido un valor")

    elif valor != '' and lista == []:
        raise ValueError("No has introducido una lista")

    elif valor == '' and lista == []:
        raise ValueError("No has introducido ningún parámetro")


if __name__ == '__main__':

    try:
        # almacena el valor introducido por el usuario
        input_usuario = int(input("Introduce un número del 1 al 20: "))

        # comprobamos que el número está entre 1 y 20
        if input_usuario >= 1 and input_usuario <= 20:

            # comprobamos si el número está en la lista
            if estaEnLista(input_usuario, lista_a_comprobar):
                print(
                    f"El número {input_usuario} se encuentra dentro de la lista"
                )

            else:
                print(
                    f"El número {input_usuario} no se encuentra dentro de la lista"
                )

        else:
            print(f"El número introducido está fuera de rango")

    except:
        print(f"El valor introducido no es válido")
