# tarifa de transporte

dia = input("¿Su dia es laborable ('S'/'N')?: ").upper
hora= float(input("Ingrese la hora del dia en el que trabajo(0-23): "))

def calcular_tarifa(dia_laborable, hora):
    if dia_laborable.upper() == "S":
        if 7 <= hora <= 9 or 17 <= hora <= 19:
            return "PICO"
        else:
            return "NORMAL"
    elif dia_laborable.upper() == "N":
        return "FIN DE SEMANA"
    else:
        return "Entrada inválida"








