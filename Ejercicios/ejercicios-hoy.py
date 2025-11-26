numero =float(input("Ingrese un numero: "))

    if numero%2==0:
        print("Es par")
    elif:
        print("Es impar")
    else:
        print("EL numero es 0")

  numero1 = float(input("Ingrese un numero: "))
  numero2 = float(input("Ingrese otro numero: "))
  numero3 = float(input("Ingrese otro numero: ")) 

  if numero1 > numero2 and numero1> numero3:
    print(f"El numero mayor es: {numero1}")
  elif numero2 > numero1 and numero2 > numero3:
    print(f"El numero mayor es: {numero2}")
  else:
    print(f"El numero mayor es: {numero3}")


    frase=input("Ingresa una frase: ")
    vocales="aeiouAEIOU"
    contador=0
    for letra in frase:
        if letra in vocales:
            contador+=1
    print(f"La cantidad de vocales en la frase es: {contador}")


    numeros = [10, 15, 20, 25, 30]
    promedio = sum(numeros)/len(numeros)
    print(f"El promedio de la lista es: {promedio}")


    datos = [1, 2, 2, 3, 4, 4, 5]
    duplicados=[]
    for i in datos:
       if i not in datos:
          sin_duplicados.append(i)
     
    print(f"Lista sin duplicados: {sin_duplicados}")


    def calculadora(num1,num2, operacion):
        if operacion == "+":
            return num1 + num2
        elif operacion == "-":
            return num1 - num2
        elif operacion == "*":
            return num1 * num2
        elif operacion == "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division por cero"
        else:
            return "Operacion no valida"


    productos = {
    "pan": 1500,
    "leche": 3000,
    "arroz": 2500
}
    max_producto = max(productos.values())")
    print(max_producto)


    texto = "este es un texto de ejemplo texto de ejemplo"
palabras = texto.split()
conteo = {}
for palabra, cantidad in conteo.items():
    print(f"{palabra}: {cantidad}")

            


from collections import Counter

# ==============================
# 1. Promedio de una lista
# ==============================
numeros = [10, 15, 20, 25, 30]
promedio = round(sum(numeros) / len(numeros), 2)
print("1) Promedio")
print(f"El promedio de la lista es: {promedio}\n")


# ==============================
# 2. Conteo de elementos duplicados
# ==============================
datos = [1, 2, 2, 3, 4, 4, 5]

conteo_datos = Counter(datos)
duplicados = sum(1 for cantidad in conteo_datos.values() if cantidad > 1)

print("2) Elementos duplicados")
print(f"La cantidad de elementos duplicados es: {duplicados}\n")


# ==============================
# 3. Calculadora avanzada
# ==============================
def calculadora(num1, num2, operacion):
    operaciones = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2 if num2 != 0 else "Error: División por cero"
    }
    return operaciones.get(operacion, "Operación no válida")


print("3) Calculadora")
print(f"10 * 5 = {calculadora(10, 5, '*')}\n")


# ==============================
# 4. Producto más caro
# ==============================
productos = {
    "pan": 1500,
    "leche": 3000,
    "arroz": 2500
}

producto_mas_caro = max(productos, key=productos.get)

print("4) Producto más caro")
print(f"{producto_mas_caro} - ${productos[producto_mas_caro]}\n")


# ==============================
# 5. Conteo de palabras en texto
# ==============================
texto = "este es un texto de ejemplo texto de ejemplo"

palabras = texto.split()
conteo_palabras = Counter(palabras)

print("5) Conteo de palabras")
for palabra, cantidad in conteo_palabras.items():
    print(f"{palabra}: {cantidad}")
