#determinar signo y paridad

numero =float(input("Ingrese un numero: "))

if numero > 0:
    print("Positivo")
    if numero%2==0:
        print("Es par")
    else:
        print("Es impar")

    if numero < 0:
      print("Negativo")
      if numero%2==0:
        print("Es par")
      else:
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