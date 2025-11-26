estudiantes={}
while True:
    nombre=input("Ingrese el nombre del estudiante: ").strip()
    if nombre.lower() =="salir":
        break
    else:
        continue
notas=[]
for i in range(1,4):
     while True:
        try:
            nota=float(input(f"Ingrese la nota {i} del estudiante: "))
            if 0<=nota<=5:
                notas.append(nota)
                break
            else:
                print("La nota debe estar entre 0 y 10")
        except ValueError:
            print("La nota debe ser un número")
            estudiantes[nombre]=notas
        for nombre, notas in estudiantes.items():
            promedio=sum(notas)/len(notas)
            if promedio>=3.5:
                print(f"El estudiante {nombre} ha aprobado con un promedio de {promedio}")
        else:
            print(f"el estudiante reprobó con un promedio de {promedio}")

def buscar_estudiante(nombre):
    if nombre in estudiantes:
        notas=estudiantes[nombre]
        promedio=sum(notas)/len(notas)
        print(f"notas: {notas}")
        print(f"promedio: {promedio}")
    else:
        print("El estudiante no se encuentra en la lista")

nombre_buscar=input("Ingrese el nombre del estudiante a buscar: ")
buscar_estudiante(nombre_buscar)

    
        
    
