
inventario={} #tupla para almacenar los datos

def agregar_producto(nombre, precio, cantidad):
    if nombre in inventario:    ## verifica si ya está agregado el producto    
        print("El producto ya existe en el inventario.")
        return
    inventario[nombre]={"precio": precio, "cantidad": cantidad}
    print(f"Producto '{nombre}' agregado correctamente.")

def consultar_producto(nombre):
    producto=inventario.get(nombre)# get para extraer el nombre de mi tupla
    if producto:
        print(f"Producto: {nombre}\nPrecio: {producto['precio']}\nCantidad: {producto['cantidad']}")
    else:
        print("El producto no existe en el inventario.")

def actualizar_precio(nombre, nuevo_precio):
    if nombre in inventario:
        inventario[nombre]["precio"]=nuevo_precio #Cambia el precio.
        print("Precio actualizado correctamente.")
    else:
        print("El producto no existe en el inventario.")

def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]#del para eliminar el producto
        print("Producto eliminado correctamente.")
    else:
        print("El producto no existe en el inventario.")

valorTotal=lambda:sum(producto["precio"]*producto["cantidad"]for producto in inventario.values()) 

def validar_float(mensaje):## funcion que retorna el mensaje para validar si es un float
    while True: 
        valor=input(mensaje)
        try:
            numero=float(valor)
            if numero<0: ##valida que no sea negativo
                print("El valor no puede ser negativo.")
            else:
                return numero
        except ValueError: 
            print("Ingresa un numero valido.")

def validar_entero(mensaje): #funcion para validar que el valor sea una cantidad entera
    while True:
        valor=input(mensaje)
        try:
            numero=int(valor)
            if numero<0:
                print("El valor no puede ser negativo.")
            else:
                return numero
        except ValueError:
            print("Ingresa un numero entero valido.")

def menu():      ## Funcion que contiene el menú que se le mostrará a el usuario.
    print("GESTION DE INVENTARIO")
    print("*"*60)
    print("1) Añadir producto")
    print("2) Consultar producto")
    print("3) Actualizar precio")
    print("4) Eliminar producto")
    print("5) Calcular valor total del inventario")
    print("6) Salir")
    print("*"*60)

while True: ##Bucle pricipal para mostrar menú y ejecutar las opciones 
     
    menu()
    print("")
    opcion = input("Selecciona una opcion: ")


#####LLamo las funciones en cada una de las opciones.
    if opcion=="1":
        print("*"*60)
        nombre=input("Nombre del producto: ").strip() #strip para eliminar espacios en blanco.
        precio=validar_float("Precio del producto: ")
        cantidad=validar_entero("Cantidad del producto: ")
        agregar_producto(nombre, precio, cantidad)

    elif opcion=="2":
        print("*"*60)
        nombre=input("Nombre del producto a consultar: ").strip()
        consultar_producto(nombre)

    elif opcion=="3":
        print("*"*60)
        nombre=input("Nombre del producto a actualizar: ").strip()
        nuevo_precio=validar_float("Nuevo precio: ")
        actualizar_precio(nombre, nuevo_precio)

    elif opcion=="4":
        print("*"*60)
        nombre=input("Nombre del producto a eliminar: ").strip()
        eliminar_producto(nombre)

    elif opcion=="5":
        print("*"*60)
        
        print("Valor total del inventario: ","$",valorTotal())

    elif opcion=="6":
        print("-"*33)
        print("Saliendo del programa... ")
        break