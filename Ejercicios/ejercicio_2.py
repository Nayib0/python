#clasificacion de edades

edad=int(input("Ingresa tu edad: "))

while edad >0:
    if edad <=18:
     print("Eres menor de edad")
     break
    elif edad >=18 and edad <=30:
     print("Eres un adulto joven")
     break  
    elif edad >=31 and edad <=65:
     print("Eres un adulto maduro")
     break
    else:
     print("Eres un adulto mayor")
     break
else: 
  print("Error, edad imposible")