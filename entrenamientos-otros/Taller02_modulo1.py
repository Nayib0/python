# Gestión de calificaciones y estadisticas.
print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
print('~~~ Gestor de calificaciones y estadisticas ~~~')
print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

nombre_usuario = input('Ingrese el nombre del usuario -> ')
nota_aprobatoria = 60

# ----- DETERMINAR ESTADO DE APROBACION -----

# Utilizamos un bucle while con la condicion True para que siempre se ejecute al inicializar el programa.
while True:
    # Comenzamos con un try para controlar que el usuario ingrese el tipo de dato correcto.
    try:
        calificacion = float(input('\nIngrese una calificación numérica (0-100) -> '))

        # Utilizamos esta condicional para controlar que la calificacion sea entre 0 y 100.
        if 0 <= calificacion <= 100:
            break # Si la condicion se cumple, terminamos el bucle while.
        else:

            # Si la condicion no se cumple, mostramos este print y el bucle vuelve a iniciar.
            print('\n***********************************************')
            print('La calificación debe estar entre 0 y 100, vuelva a intentarlo')
            print('***********************************************\n')

    # Si el tipo de dato ingresado por el usuario es diferente a float, entrará en el except, imprimirá el 
    # mensaje y el bucle volverá a iniciar.
    except ValueError:
        print('\n***********************************************')
        print('Por favor, ingrese un número entero válido!')
        print('***********************************************\n')

# Utilizamos esta condicional para verificar si el usuario aprobó o reprobó.
if calificacion >= nota_aprobatoria:
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    print(f'Felicitaciones {nombre_usuario}, has aprobado con {calificacion} 🥳🥳!')
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
else:
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    print(f'Lo sentimos {nombre_usuario}, has reprobado con {calificacion} 😢😢')
    print(f'Solo te faltaron {nota_aprobatoria - calificacion} puntos mas para aprobar.')
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')


# ----- CALCULAR PROMEDIO -----

# Utilizamos un bucle while con la condicion True para que siempre se ejecute al inicializar el programa.
while True:
    # Comenzamos con un try para controlar que el usuario ingrese el tipo de dato correcto.
    try:
        # Creamos una variable la cual recogerá en una cadena de texto todas las calificaciones a promediar separadas por comas
        input_calificaciones = input('Ingrese las calificaciones separadas por comas (,) -> ')
        '''
            Creamos una lista en la cual recorreremos todas las notas separadas por comas del input anterior.
            Usamos el metodo split() con el parametro (',') en el cual le estamos indicando que la coma es el separador entre cada elemento.
            En cada iteracion, utilizaremos el metodo strip() el cual nos eliminará el espacio en blanco que tenga cada calificacion.
        '''
        lista_calificaciones = [float(calificaciones.strip()) for calificaciones in input_calificaciones.split(',')]

        # Utilizamos la funcion all() la cual nos dará un valor booleano, el cual solo será True si todos los elementos de la lista dan True a la condicion que le damos
        if all(0 <= calificaciones <= 100 for calificaciones in lista_calificaciones):
            if lista_calificaciones:
                # Si la lista existe, sacaremos el promedio con las funciones sum() y len()
                promedio = sum(lista_calificaciones) / len(lista_calificaciones)

                if promedio >= nota_aprobatoria:
                    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
                    print(f'Felicidades {nombre_usuario}, has aprobado con un promedio de {promedio:.2f} 🥳🥳!')
                    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
                    break
                else:
                    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
                    print(f'Lo sentimos {nombre_usuario}, has reprobado con un promedio de {promedio:.2f} 😢😢!')
                    print(f'Solo te faltaron {(nota_aprobatoria - promedio):.2f} puntos mas para aprobar.')
                    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
                    break
        else:
            print('\n**********************************************************************')
            print('Todas las calificaciones deben estar entre 0-100, intente nuevamente!')
            print('**********************************************************************\n')
    except ValueError:
        print('\n*******************************************************************************')
        print('Por favor, ingrese las calificaciones separadas por comas y en numeros enteros!')
        print('*******************************************************************************\n')


# CONTADOR DE CALIFICACIONES MAYORES.

# Utilizamos un bucle while con la condicion True para que siempre se ejecute al inicializar el programa.
while True:
    # Comenzamos con un try para controlar que el usuario ingrese el tipo de dato correcto.
    try:
        calificacion_comparacion = float(input('Ingrese calificacion base para buscar -> '))
        break
    except ValueError:
        print('\n********************************************')
        print('Por favor, ingrese un número entero válido.')
        print('********************************************\n')
print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
contador = 0
# Utilizamos un for para recorrer todas las calificaciones dentro de la lista
for calificacion in lista_calificaciones:

    # Utilizamos while con esta condicion en especifico para que solo se ejecute cuando uan calificacion sea mayor a la calificacion a comparar
    while calificacion > calificacion_comparacion:

        # Una vez la condicion se cumpla, imprimiremos en pantalla la calificacion mayor y se sumará 1 a el contador
        print(f'La calificacion {calificacion} es mayor a {calificacion_comparacion}')
        contador += 1
        break # Rompemos el ciclo para que no se vuelva infinito cada vez que se ejecute el ciclo

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
print(f'Hay {contador} calificaciones mayores que {calificacion_comparacion}.')
print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

# VERIFICADOR Y CONTADOR DE CALIFICACIONES ESPECÍFICAS.

# Utilizamos un bucle while con la condicion True para que siempre se ejecute al inicializar el programa.
while True:
    # Comenzamos con un try para controlar que el usuario ingrese el tipo de dato correcto.
    try:
        calificacion_especifica = float(input('Ingrese la calificacion especifica a buscar -> '))
        if 0 <= calificacion_especifica <= 100:
            break
        else:
            print('\n************************************************************')
            print('La calificacion debe estar entre 0-100, intente nuevamente!')
            print('************************************************************\n')
        
    except ValueError:
        print('\n********************************************')
        print('Por favor, ingrese un número entero válido.')
        print('********************************************\n')

# Inicio contador en 0 y coincidida en False como valor por defecto.
contador = 0
coincidida = False

# Utilizamos un for para recorrer cada elemento de nuestra lista de calificaciones.
for calificacion in lista_calificaciones:
    if calificacion == calificacion_especifica:

        # Si calificacion es igual a la calificacion especifica que ingresó el usuario, sumaremos 1 al contador y cambiaremos el valor de coincidida a True.
        contador += 1
        coincidida = True

    continue # Continua con la siguiente iteración incluso si se encuentra la calificacion.

# Utilizamos un condicional el cual dependiento del resultado de la busqueda anterior, nos imprimirá si hubieron coincidencias o no.
if coincidida:
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    print(f'La calificación {calificacion_especifica} aparece {contador} veces en la lista.')
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
else:
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    print(f'La calificación {calificacion_especifica} no se encontró en la lista.')
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

