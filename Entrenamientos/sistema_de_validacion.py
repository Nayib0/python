#programa que calcula el costo total de una compra
print("Bienvenido al sistema de validación de su compra")
nombre_cliente=(input("ingrese su nombre: "))

# pedimos los datos al usuario necesarios para calcular el costo total de la compra
print("\nBienvenido al sistema ",(nombre_cliente))

nombre = (input("\nIngrese el nombre del producto: "))
precio = float(input("Ingrese el precio del producto: "))

while precio < 0 or precio == 0:
    print("\nEl precio no puede ser menor a 1")
    precio = float(input("Ingrese el precio del producto: "))

#validamos la cantidad de productos           
cantidad = int(input("Ingrese la cantidad de productos: "))
while cantidad < 0 or cantidad == 0:
    print("\nLa cantidad no puede ser menor a 1")
    cantidad = int(input("Ingrese la cantidad de productos: "))

#validamos el descuento

descuento = int(input("Ingrese el descuento del producto: (0 si no aplica): "))
while descuento < 0 or descuento > 100:
    print("\nEl descuento no puede ser menor a 0 o mayor a 100")
    descuento = int(input("Ingrese el descuento del producto: (0 si no aplica): "))

# mostramos los datos ingresados por el usuario

print("\nTu producto es: ",(nombre))
print("\nEl precio es: ",(precio))
print("\nLa cantidad es: ", (cantidad))
print(f"\nTu descuento es de:  {descuento:.0f}%")

# calculamos el costo total de la compra

costo_total = (precio * cantidad)
print(f"\nEl costo total es: {costo_total:.2f}")

# calculamos el descuento si lo tiene

while descuento > 0 and descuento < 100:
    descuento_total = (costo_total * descuento) / 100
    print("\nEl costo total con descuento es: ", (costo_total-descuento_total))
    break

respuesta = input("¿Desea realizar otra compra? (si/no): ")
while respuesta != "si" and respuesta != "no":
    print("Respuesta inválida. Ingrese 'si' o 'no'.")
    respuesta = input("¿Desea realizar otra compra? (si/no): ")

if respuesta == "si":
    print("Perfecto, continuemos")
    # Aquí podrías reiniciar el flujo, si lo deseas
else:
    print("Gracias por su compra")

# generamos mensaje por si desea conocer su factura

respuesta =(input("Desea conocer su factura? (si/no): "))
if respuesta == "si" :
    print("\n ----Su factura es:---- ")
    print("Nombre del cliente: ",   (nombre_cliente))
    print("\nNombre del producto: ",  (nombre))
    print("Precio del producto: ",     (precio))
    print("Cantidad de productos: ",   (cantidad))
    print("Descuento del producto: ",  (descuento))
    print("Costo total de la compra: ", (costo_total))

elif respuesta == "no":
    print("Gracias por su compra")
else:
        print("Respuesta invalida")
#fin del programa

    