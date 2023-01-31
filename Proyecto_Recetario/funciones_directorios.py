# Importaciones
from pathlib import Path
import os
from os import system, remove
from shutil import rmtree

# Configuración de rutas -----------------------------------------------------------------------------------------------
# Ruta base
base = 'C:/Users/Alberto Alonso/Documents/Desarrolador en Programación/PYTHON DEVELOPER/Python Avanzado/Día 6'

# Ruta al recetario
ruta_recetario = Path(base, 'Recetas')


# Función de incio del programa ----------------------------------------------------------------------------------------
def inicio(ruta):
    """
    Esta función toma la ruta de ubicación de los archivos y muestra las opciones del programa, regresando el número de
    la petición del ususario a ejecutar.
    :param ruta: Ruta de ubicación de archivos del recetario.
    :return: Petición del ususario.
    """

    # Conteo de recetas
    count = 0
    for txt in Path(ruta).glob('**/*.txt'):
        count += 1

    print('Bienvenido al Recetario.')
    print(f'La ruta de acceso al recetario es: {ruta}' + '\n')
    print(f'Hay un total de {count} recetas en la carpeta.')

    # Aseguramiento de valor correcto ingresado
    peticion = 0
    while peticion not in range(1, 7):
        # Petición de opciones
        peticion = input('Por favor elige una de las siguientes opciones disponibles' + '\n' +
                         '[1] - Leer receta' + '\n' +
                         '[2] - Crear receta' + '\n' +
                         '[3] - Crear categoría' + '\n' +
                         '[4] - Eliminar receta' + '\n' +
                         '[5] - Eliminar categoría' + '\n' +
                         '[6] - Finalizar programa' + '\n' +
                         'Elección: ')
        peticion = int(peticion)

    return peticion


# Función para mostrar categorías --------------------------------------------------------------------------------------
def mostrar_cat(ruta):
    """
    Esta función toma la ruta de ubicación del recetario, mostrando y regresando todas las categorías existentes en el
    recetario.
    :param ruta: Ruta de ubicación del recetario.
    :return: Lista de las categorías en el recetario.
    """
    categorias = []
    for dir in ruta.iterdir():
        categorias.append(dir.name)
        print(dir.name)

    return categorias


# Función para asegurar de que existen ficheros en una categoría -------------------------------------------------------
def aseguramiento(ruta):
    """
    Esta función se asegura de que existan ficheron en una determinada categoría, si existen se continúa con la petición
    del usuario, de lo contrario esta función mostrará un mensaje al usuario y terminará la ejecución de la opción
    seleccionada.
    :param ruta: Ruta de la carpeta de la categoría especificada por el usuario.
    :return: Retorno vacío sí existen ficheros en la ruta, en caso contrario retorna calor de 1 como entero .
    """
    cont = 0
    for txt in Path(ruta).glob('*.txt'):
        cont += 1
    if cont == 0:
        print('\n')
        print('No existen recetas de esta categoría aún.')
        return 1


# Función de Opción 1 --------------------------------------------------------------------------------------------------
def opcion_1(ruta_op1):
    """
    Esta función lee una receta específica del recetario, a partir de la selección específica de categoría y receta a
    petición del ususario.
    :param ruta_op1: Ruta donde se encuentra la carpeta que contiene al recetario.
    :return: Imprime la lectura del archivo correspondiente a la receta seleccionada, en caso de no existir ficheros en
    la categoría seleccionada entrega un retorno vacío.
    """
    print('\n')
    print('Las categorías que se tienen de las recetas son:')

    # Mostrar categorías.
    categorias = mostrar_cat(ruta_op1)

    # Petición de categoría.
    categoria = ''
    while categoria not in categorias:
        categoria = input('¿Qué categoría te gustaría elegir?: ')

    # Armado de ruta apuntando a la categoría especificada.
    else:
        ruta_categoria = Path(ruta_op1, categoria)

        # Aseguramiento de que existan ficheros en la categoría.
        i = aseguramiento(ruta_categoria)
        if i == 1:
            return

        # Mostrar recetas de la categoría.
        print('\n')
        print(f'Las recetas que se tienen de la categoría {categoria} son: ')

        ficheros_nombre = []
        ficheros_completo = []
        for fichero in ruta_categoria.iterdir():
            ficheros_completo.append(fichero.name)
            ficheros_nombre.append(fichero.stem)
            print(fichero.stem)

        # Petición de receta.
        receta = ''
        while receta not in ficheros_nombre:
            receta = input('¿Qué receta te gustaría leer?: ')

        # Armado de ruta apuntando a la categoría especificada.
        else:
            for fichero in ficheros_completo:
                indice = fichero.index('.')
                fichero_stem = fichero[:indice]

                if receta == fichero_stem:
                    ruta_receta = Path(ruta_categoria, fichero)

                    receta_op1 = open(ruta_receta)

                    print('\n')
                    print(receta_op1.read())

                    receta_op1.close()


# Función de Opción 2 --------------------------------------------------------------------------------------------------
def opcion_2(ruta_op2):
    """
    Esta función permite agregar una nueva receta al recetario, dentro de una categoría previamente especificada por el
    usuario.
    :param ruta_op2: Ruta donde se encuentra la carpeta que contiene al recetario.
    :return: Retorno vacío, e impresión de mensaje de confirmación de que la receta especificada ha sido agregada en el
    recetario.
    """
    print('\n')
    print('Las categorías que se tienen de las recetas son:')

    # Mostrar categorías.
    categorias = mostrar_cat(ruta_op2)

    # Petición de categoría.
    categoria = ''
    while categoria not in categorias:
        categoria = input('¿Qué categoría te gustaría elegir?: ')

    # Armado de ruta apuntando a la categoría especificada.
    else:
        ruta_categoria = Path(ruta_op2, categoria)

        # Petición y creación del nombre de la nueva receta.
        print('\n')
        nuevo_nombre = input('¿Cuál es el nombre de la receta de que desea agregar?: ')
        ruta_nueva_receta = Path(ruta_categoria, nuevo_nombre + '.txt')
        nuevo_archivo = open(ruta_nueva_receta, 'w')

        # Petición de contenido de receta.
        print('\n')
        contenido_receta = input(f'¿Cuál es el contenido de la receta de {nuevo_nombre}?: ')
        nuevo_archivo.write(contenido_receta)

        nuevo_archivo.close()

        print('\n')
        print(f'La receta, {nuevo_nombre}, ha sido agregada exitosamente a la categoría {categoria}, en el recetario.')


# Función de Opción 3 --------------------------------------------------------------------------------------------------
def opcion_3(ruta_op3):
    """
    Esta función permite crear una nueva categoría (carpeta) dentro del recetario.
    :param ruta_op3: Ruta donde se encuentra la carpeta que contiene al recetario.
    :return: Retorno vacío, e impresión de mensaje de confirmación de que la categoría especificada ha sido creada.
    """
    print('\n')
    print('Las categorías que se tienen de las recetas son:')

    # Mostrar categorías.
    mostrar_cat(ruta_op3)

    # Petición del nombre y de la nueva categoría.
    print('\n')
    nueva_categoria = input('¿Cuál será el nombre de la nueva categoría?: ')
    ruta_nueva_categoria = Path(ruta_op3, nueva_categoria)
    os.makedirs(ruta_nueva_categoria)

    print('\n')
    print(f'La categoría, {nueva_categoria}, ha sido agregada exitosamente al recetario.')


# Función de Opción 4 --------------------------------------------------------------------------------------------------
def opcion_4(ruta_op4):
    """
    Esta función permite al usuario eliminar una receta específica del recetario, a partir de la selección específica de
    categoría y receta a petición del ususario.
    :param ruta_op4: Ruta donde se encuentra la carpeta que contiene al recetario.
    :return: Retorno vacío, e impresión de mensaje de confirmación de que la receta especificada ha sido eliminada en el
    recetario.
    """
    print('\n')
    print('Las categorías que se tienen de las recetas son:')

    # Mostrar categorías.
    categorias = mostrar_cat(ruta_op4)

    # Petición de categoría.
    categoria = ''
    while categoria not in categorias:
        categoria = input('¿Qué categoría te gustaría elegir?: ')

    # Armado de ruta apuntando a la categoría especificada.
    else:
        ruta_categoria = Path(ruta_op4, categoria)

        # Aseguramiento de que existan ficheros en la categoría.
        i = aseguramiento(ruta_categoria)
        if i == 1:
            return

        # Mostrar recetas de la categoría.
        print('\n')
        print(f'Las recetas que se tienen de la categoría {categoria} son: ')

        ficheros_nombre = []
        ficheros_completo = []
        for fichero in ruta_categoria.iterdir():
            ficheros_completo.append(fichero.name)
            ficheros_nombre.append(fichero.stem)
            print(fichero.stem)

        # Petición de receta.
        receta = ''
        while receta not in ficheros_nombre:
            receta = input('¿Qué receta te gustaría eliminar?: ')

        # Armado de ruta apuntando a la categoría especificada.
        else:
            for fichero in ficheros_completo:
                indice = fichero.index('.')
                fichero_stem = fichero[:indice]

                if receta == fichero_stem:
                    ruta_receta = Path(ruta_categoria, fichero)

                    remove(ruta_receta)

                    print('\n')
                    print(f'La receta, {receta}, ha sido eliminada exitosamente de la categoría {categoria}, en el '
                          f'recetario.')


# Función de Opción 5 --------------------------------------------------------------------------------------------------
def opcion_5(ruta_op5):
    """
    Esta función permite eliminar de una nueva categoría (carpeta) dentro del recetario.
    :param ruta_op5: Ruta donde se encuentra la carpeta que contiene al recetario.
    :return: Retorno vacío, e impresión de mensaje de confirmación de que la categoría especificada ha sido eliminada.
    """
    print('\n')
    print('Las categorías que se tienen de las recetas son:')

    # Mostrar categorías.
    categorias = mostrar_cat(ruta_op5)

    # Petición de categoría.
    categoria_eliminada = ''
    while categoria_eliminada not in categorias:
        categoria_eliminada = input('¿Qué categoría desea eliminar?: ')

    # Eliminación de la categoría seleccionada.
    else:
        ruta_categoria_eliminada = Path(ruta_op5, categoria_eliminada)

        # Revisión de existencia de ficheros en la categoría especificada.
        count = 0
        for txt in Path(ruta_categoria_eliminada).glob('*.txt'):
            count += 1

        # Si la carpeta tiene ficheros.
        if count != 0:
            rmtree(ruta_categoria_eliminada)
        else:
            # Si la carpeta no tiene ficheros
            os.rmdir(ruta_categoria_eliminada)

        print('\n')
        print(f'La categoría, {categoria_eliminada}, ha sido eliminada exitosamente al recetario.')


# Ejecución de funciones por petición ----------------------------------------------------------------------------------
def funciones(case_selector):
    """
    Esta función ejecuta la opción seleccionada por el ususario, y posteriormente define si el usuario desea ejecutar
    una nueva acción o no.
    :param case_selector: Número de opción seleccionada que el usuario desea ejecutar.
    :return: Respuesta de sí el usuario desea o no continuar y ejecutar una nueva acción.
    """
    # rompimiento de ciclo while por petición.
    if case_selector == 1:
        opcion_1(ruta_recetario)
    elif case_selector == 2:
        opcion_2(ruta_recetario)
    elif case_selector == 3:
        opcion_3(ruta_recetario)
    elif case_selector == 4:
        opcion_4(ruta_recetario)
    elif case_selector == 5:
        opcion_5(ruta_recetario)
    else:
        return 'n'

    print('\n')
    decision = input('¿Deseas realizar alguna otra acción? [y/n]: ')
    if decision == 'y':
        system('cls')
    else:
        pass

    return decision


# Cuerpo del programa --------------------------------------------------------------------------------------------------
respuesta = 'y'

# Ejecución e inicio del programa.
while respuesta != 'n':

    # Inicio del programa.
    selection = inicio(ruta_recetario)

    # Ejecución de funciones por petición.
    respuesta = funciones(selection)

# Finalización del programa.
else:
    print('\n')
    print('Hasta luego, vuelva pronto.')
    print('Programa finalizado.')
