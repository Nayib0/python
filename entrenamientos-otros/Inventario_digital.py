# --- Inventario digital ---

# Función para mostrar el menú principal de opciones
def mostrar_menu():
    print("\n--- Options ---")
    print("1. Add product")                       # Opción para añadir un nuevo producto o actualizar uno existente
    print("2. Looking for product")                  # Opción para consultar los datos de un producto específico
    print("3. Update value")                   # Opción para cambiar el precio de un producto existente
    print("4. Delete product")                   # Opción para borrar un producto del inventario
    print("5. Calculate total value") # Opción para obtener el valor total del inventario
    print("6. Show all the products")         # Opción para listar todos los productos almacenados
    print("7. Leave")                               # Opción para salir del programa

# Función para añadir un nuevo producto al inventario
def añadir_producto(inventario):
    nombre = input("Product name: ").strip()  # Solicita el nombre del producto y elimina espacios al inicio/final
    if not nombre:  # Verifica que el nombre no esté vacío
        print("the product name can't be empty.")
        return
    try:
        precio = float(input("product value: "))       # Solicita el precio (número decimal)
        cantidad = int(input("amount available: "))       # Solicita la cantidad (número entero)
        if precio < 0 or cantidad < 0:                       # Valida que los valores no sean negativos
            raise ValueError
    except ValueError:
        print("price and amount must be numbers availables")
        return

    if nombre in inventario:  # Si el producto ya existe, actualiza la cantidad y el precio
        print("the product already exist. the amount and price will be update")
        inventario[nombre] = (precio, inventario[nombre][1] + cantidad)
    else:  # Si es un producto nuevo, lo agrega al inventario
        inventario[nombre] = (precio, cantidad)
    print(f"product '{nombre}' add/update correctly.")

# Función para consultar los datos de un producto específico
def consultar_producto(inventario):
    nombre = input("insert the product name to check: ").strip()  # Solicita el nombre del producto
    producto = inventario.get(nombre)  # Busca el producto en el inventario
    if producto:
        precio, cantidad = producto
        print(f"{nombre} - price: ${precio:.2f}, amount available: {cantidad}")
    else:
        print("Product not found.")

# Función para actualizar solo el precio de un producto
def actualizar_precio(inventario):
    nombre = input("insert the name to update: ").strip()
    if nombre in inventario:
        try:
            nuevo_precio = float(input("insert the new price: "))  # Solicita el nuevo precio
            if nuevo_precio < 0:
                raise ValueError
            cantidad = inventario[nombre][1]  # Conserva la cantidad actual
            inventario[nombre] = (nuevo_precio, cantidad)  # Actualiza el precio
            print(f"price '{nombre}' update to ${nuevo_precio:.2f}")
        except ValueError:
            print("the price must be a decimal number available and no negative.")
    else:
        print("Product not found.")

# Función para eliminar un producto del inventario
def eliminar_producto(inventario):
    nombre = input("Insert the product name to delete: ").strip()
    if nombre in inventario:
        confirmacion = input(f"¿are yyou sure to delete '{nombre}'? (y/n): ").strip().lower()
        if confirmacion == 'y':  # Confirma la eliminación
            del inventario[nombre]  # Elimina el producto
            print(f"Product '{nombre}' deleted to the inventory.")
        else:
            print("canceled.")
    else:
        print("Product not found.")

# Función para calcular el valor total del inventario
def calcular_valor_total(inventario):
    # Multiplica el precio por la cantidad de cada producto y suma los totales
    valor_total = sum(map(lambda item: item[0] * item[1], inventario.values()))
    print(f"total inventory value: ${valor_total:.2f}")

# Función para mostrar todos los productos del inventario
def mostrar_todos_los_productos(inventario):
    if not inventario:
        print("The inventory is empty.")
        return
    print("\nList of products in inventory:")
    for nombre, (precio, cantidad) in inventario.items():
        print(f"- {nombre}: ${precio:.2f}, amount: {cantidad}")

# Función principal que ejecuta el programa
def main():
    inventario = {}  # Diccionario vacío para almacenar los productos
    while True:  # Bucle infinito hasta que el usuario elija salir
        mostrar_menu()  # Muestra el menú de opciones
        opcion = input("choose an option (1-7): ").strip()  # Solicita la opción del usuario

        # Ejecuta la función correspondiente según la opción elegida
        if opcion == '1':
            añadir_producto(inventario)
        elif opcion == '2':
            consultar_producto(inventario)
        elif opcion == '3':
            actualizar_precio(inventario)
        elif opcion == '4':
            eliminar_producto(inventario)
        elif opcion == '5':
            calcular_valor_total(inventario)
        elif opcion == '6':
            mostrar_todos_los_productos(inventario)
        elif opcion == '7':
            print("Leaving ¡come soon!")  # Mensaje de despedida
            break  # Termina el bucle y el programa
        else:
            print("Wrong option. please, choose an option between 1 to 7.")  # Maneja entradas inválidas

# Condición para ejecutar el programa solo si se ejecuta directamente (no como módulo)
if __name__ == "__main__":
    main()