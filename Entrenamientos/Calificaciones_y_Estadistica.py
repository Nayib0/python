print("BIENVENIDO A SU CONTROL DE CALIFICACIONES Y ESTADISTICAS")
# Primera nota y validacion
while True:
  try:
   calificacion= float(input("Ingresa una nota (0/100): "))
   

   if 0<= calificacion <=100:
     break
   else:
     print("El valor debe estar entre (0/100)")
   
  except:
   print("El valor debe ser numérico")

# Pedimos las calificaciones y le mostramos el promedio de todas las calificaciones

while True:  
      try:
        notas= input("\nIngresa el total de sus calificaciones separadas por comas: ").split(",")
        lista_calificaciones=[float(nota.strip())for nota in notas]
        print(f"\nLas calificaciones que tienes son: {lista_calificaciones}")

        promedio=sum(lista_calificaciones)/len(lista_calificaciones)
        print("-"*70)
        print("Valor minimo para pasar es: 70 puntos")
        print("-"*70)
        print(f"\nEl promedio de todas tus notas son: {promedio:.2f} puntos")
        if promedio<70:
          print("Promedio muy bajito, debes mejorarlo")
          print("-"*70)
        else:
          print("Muy bien, debes mantenerte")

      except ValueError:
        print("El valor debe ser numérico")
   
 # Pedimos un numero y vemos que calificaciones están por encima de ese numero

      while True:
        try:
          valor_comparativo=float(input("\nIngrese el valor a comparar: "))
          break
        except ValueError:
          print("El valor debe ser numérico")

      contador=0
        
      for calificacion in lista_calificaciones:

        while calificacion > valor_comparativo:

            # Una vez la condicion se cumpla, imprimiremos en pantalla la calificacion mayor y se sumará 1 a el contador
            
            print(f"{calificacion} es mayor a {valor_comparativo}")
            contador += 1
            break 
      print(f"\nTenemos {contador} calificaciones mayores a {valor_comparativo}")
      

    # Pedimos al usuario que nos ingrese una de sus calificaciones y procedemos a mostrar la cantidad de veces que se repite
      repetidas= int(input("\nIngresa la calificaion que deseas ver la cantidad de veces que se encuentra repetida: "))

      contador_repetidas=0
            
      for calificacion in lista_calificaciones:
            if calificacion == repetidas:
              contador_repetidas+=1
              continue
      if contador_repetidas==1:
        print(f"\n{repetidas} se encuentra {contador_repetidas} vez")
      else:
          print(f"\n{repetidas} se encuentra {contador_repetidas} veces")
            
    # Mostramos la nota mas alta y mas baja de la lista

      print("\n MOSTRAMOS LA CALIFICACION MAS ALTA Y MAS BAJA")
      print(f"\nLa nota más alta es: {max(lista_calificaciones)}\n")
      print(f"La nota más baja es: {min(lista_calificaciones)}")

      print("\n Gracias por confiar en nosotros, vuelva pronto...")
      break
           










         






















     


      
   
 







































