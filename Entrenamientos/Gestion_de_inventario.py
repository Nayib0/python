# Gestión de inventario de una tienda
# Diccionario vacío para almacenar los datos
inventario= {}

# Definimos las funciones que vamos a utilizar para así llamarlas cuando las necesite

def agregar_producto(nombre, precio, cantidad):
    print("-"*33)
    if nombre in inventario:
         print("El producto ya existe")
         return 
    inventario [nombre] ={"precio" : precio, "cantidad": cantidad}
    print(f"{nombre} agregado/a al inventario")


def consultar_productos(nombre):
    print("-"*33)
    producto=inventario.get(nombre)
    if producto:
        print(f"Producto: \n{nombre} Precio: \n{producto['precio']} Cantidad: \n{producto['cantidad']}")
    else:
        print("Producto no encontrado en el inventario")

def actualizar_precios(nombre, precio_nuevo):
    print("-"*33)
    if nombre in inventario:      
        inventario[nombre]["precio"]= precio_nuevo
        print(inventario)
        print(f"Precio de '{nombre}' actualizado/a")
    else:
        print("El producto no está disponible en nuestro inventario")


def eliminar_productos(nombre):
    print("-"*33)
    if nombre in inventario:
      del inventario[nombre]
      print(f"{nombre} eliminado del inventario")
    else: 
      print(f"Producto {nombre} no encontrado en inventario")

# Usamos una funcion temporal(lambda) para calcular el valor total
valor_total=lambda:sum(producto["precio"]*producto["cantidad"] for producto in inventario.values())

# Definimos una funcion para validar el ingreso de datos y luego agregarla cuando sea necesaria
def validar_float(entrada):
    while True: 
        valor=input(entrada).strip()
        try:
            numero=float(valor)
            if numero<0: 
                print("El valor no puede ser negativo.")
            else:
                return numero
        except ValueError: 
            print("Debe ser un valor numérico")

def validar_int(entrada): 
    while True:
        valor=input(entrada)
        try:
            numero=int(valor)
            if numero<0:
                print("El valor no puede ser negativo.")
            else:
                return numero
        except ValueError:
            print("Debe ser un valor numérico")            

# Mostramos el menú de opciones y pedimos al usuario que elija algún valor
while True:
  print("-"*33)
  print("\t MENÚ DE LA TIENDA \n")      
  print("-"*33)
  print("1. Agregar producto")
  print("2. Consultar producto")
  print("3. Actualizar precio")
  print("4. Eliminar producto")
  print("5. Calcular valor total")
  print("0. Salir")
  print("-"*33)
  try:
   seleccion = int(input("Seleccione una opcion del menú: ").strip())
   print("-"*33)

  except ValueError:
    print("Debe ser un valor numérico")
    continue
  try:
    if seleccion == 1:
            nombre=input("Ingrese el nombre del producto: ").strip().lower()
            precio=validar_float("Ingrese el precio del producto: ")
            cantidad=validar_int("Ingresa la cantidad del producto: ")
            agregar_producto(nombre, precio, cantidad)

    elif seleccion == 2:
            nombre=input("Ingrese el nombre del producto a consultar: ").strip().lower()
            consultar_productos(nombre)

    elif seleccion== 3:
            nombre=input("Nombre del producto a actualizar: ").strip().lower()
            precio_nuevo=validar_float("Ingrese el nuevo precio: ")
            actualizar_precios(nombre, precio_nuevo)

    elif seleccion == 4 :
            nombre=input("Escriba el nombre del producto que desea eliminar:  ").strip()
            eliminar_productos(nombre)

    elif seleccion == 5:
            print("Valor total del inventario es:", valor_total())
     
    elif seleccion == 0:
            print("Muchas gracias por visitarnos")
            break
    else:
            print("Valor no encontrado, escriba una opción disponible") 
  except ValueError:
    print("Debe ser un valor numérico")

  








