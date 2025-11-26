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

  number = float(input("Ingrese un numero: "))  

  number%2==0 "es par"?