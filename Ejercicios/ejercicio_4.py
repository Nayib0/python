monto = float(input("Ingrese el monto de la compra: "))
vip= input(" Es usted vip ('S'/'N')")

if vip.upper =='S': 
 if monto >= 500:
    print("Tienes un 20'%' de descuento")
 else:
   print("Tienes un 10'%' de descuento")