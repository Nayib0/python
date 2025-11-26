contactos = {}

def agregar_contacto():
    nombre = input("Hola, ¿cuál es tu nombre? \n").strip().capitalize()
    telefono = input("¿Cuál es tu número de teléfono? \n")
    correo = input("¿Cuál es tu correo electrónico? \n")
    contactos[nombre] = {"telefono": telefono, "correo": correo}
    print("Contacto agregado satisfactoriamente.")

def buscar_contacto():
    nombre = input("¿Qué contacto deseas buscar? \n").strip().capitalize()
    if nombre in contactos:
        print(f"📞 Nombre: {nombre}")
        print(f"   Teléfono: {contactos[nombre]['telefono']}")
        print(f"   Correo: {contactos[nombre]['correo']}")
    else:
        print("Contacto no encontrado.")

def modificar_contacto():
    nombre = input("¿Qué contacto deseas modificar? \n").strip().capitalize()
    if nombre in contactos:
        telefono = input("Ingresa el número de teléfono: \n").strip()
        correo = input("Ingresa el correo electrónico: \n").strip()
        contactos[nombre] = {"telefono": telefono, "correo": correo}
        print("Contacto modificado satisfactoriamente.")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto():
    nombre = input("Ingresa el contacto a eliminar: \n").strip().capitalize()
    if nombre in contactos:
        del contactos[nombre]
        print("Contacto eliminado.")
    else:
        print("Contacto no encontrado.")

def mostrar_contactos():
    if not contactos:
        print("No hay contactos agendados.")
    else:
        print("\n📇 Lista de contactos:")
        for nombre, info in contactos.items():
            print(f"Nombre: {nombre}, Teléfono: {info['telefono']} | Correo: {info['correo']}")

def menu():
    while True:
        print("\n--- Menú de Gestión de Contactos ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Modificar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos los contactos")
        print("0. Salir")
        
        try:
            opcion = int(input("Selecciona una opción:   "))
        except ValueError: 
            print("Por favor, digita un número válido.")
            continue
         
        if opcion == 1:
            agregar_contacto()
        elif opcion == 2:
            buscar_contacto()    
        elif opcion == 3:
            modificar_contacto()
        elif opcion == 4:
            eliminar_contacto()
        elif opcion == 5:
            mostrar_contactos()
        elif opcion == 0: 
            print("Fue un gusto, ¡hasta luego!")
            break
        else:
            print("Por favor, digita un número válido.")

menu()
