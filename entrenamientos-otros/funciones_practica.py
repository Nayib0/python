def preparar_pollo_a_la_plancha(presentacion):
    """
    Prepara el pollo a la plancha según la presentación indicada.

    Parámetros:
    - presentacion (str): "tiras" o "normal".

    Retorna:
    - str: Descripción del pollo preparado.
    """
    if presentacion == "tiras":
        return "Tiras de pechuga de pollo a la plancha"
    elif presentacion == "normal":
        return "Pechuga de pollo a la plancha"
    else:
        return "Presentación no válida"

def preparar_salsa_cesar(pimienta_negra_molida):
    """
    Prepara la salsa César con o sin pimienta negra.

    Parámetros:
    - pimienta_negra_molida (bool): True si se desea con pimienta negra, False si no.

    Retorna:
    - dict: Ingredientes de la salsa.
    """
    return {
        "pimienta_negra": pimienta_negra_molida,
        "sal": "al gusto",
        "zumo_limon": "10 ml"
    }

def preparar_ensalada_cesar_con_pollo():
    """
    Prepara la ensalada César con pollo.

    Retorna:
    - dict: Información detallada de la receta.
    """
    pollo = preparar_pollo_a_la_plancha("tiras")
    salsa = preparar_salsa_cesar(True)
    ingredientes = ["lechuga romana", "tomates cherry", "crutones", "queso parmesano", "pollo"]
    pasos = [
        "Lavar y cortar la lechuga.",
        "Cortar los tomates cherry por la mitad.",
        "Mezclar la lechuga, tomates, crutones y queso.",
        "Añadir el pollo a la mezcla.",
        "Verter la salsa César sobre la ensalada."
    ]
    return {
        "receta": "ensalada_cesar_con_pollo",
        "salsa": salsa,
        "presentacion_pollo": "tiras",
        "ingredientes": ingredientes,
        "pasos": pasos
    }

def preparar_wrap_pollo():
    """
    Prepara el wrap de pollo.

    Retorna:
    - dict: Información detallada de la receta.
    """
    pollo = preparar_pollo_a_la_plancha("normal")
    salsa = preparar_salsa_cesar(False)
    ingredientes = ["tortilla de trigo", "lechuga", "tomates cherry", "queso rallado", "pollo", "salsa César"]
    pasos = [
        "Calentar la tortilla en una sartén.",
        "Colocar la lechuga, tomates, queso y pollo en el centro.",
        "Añadir la salsa César.",
        "Enrollar la tortilla formando el wrap."
    ]
    return {
        "receta": "wrap_de_pollo",
        "salsa": salsa,
        "presentacion_pollo": "normal",
        "ingredientes": ingredientes,
        "pasos": pasos
    }

def preparar_sandwich_clasico():
    """
    Prepara el sándwich clásico de pollo.

    Retorna:
    - dict: Información detallada de la receta.
    """
    pollo = preparar_pollo_a_la_plancha("normal")
    salsa = preparar_salsa_cesar(True)
    ingredientes = ["pan de sándwich", "lechuga", "tomate", "queso", "pollo", "salsa César"]
    pasos = [
        "Tostar ligeramente el pan.",
        "Colocar la lechuga, tomate y queso en una rebanada de pan.",
        "Añadir el pollo.",
        "Verter la salsa César sobre el pollo.",
        "Cubrir con la otra rebanada de pan."
    ]
    return {
        "receta": "sandwich_clasico",
        "salsa": salsa,
        "presentacion_pollo": "normal",
        "ingredientes": ingredientes,
        "pasos": pasos
    }

def emplatado(receta):
    """
    Retorna la información detallada de la receta seleccionada.

    Parámetros:
    - receta (str): Nombre de la receta.

    Retorna:
    - dict: Información detallada de la receta.
    """
    if receta == "ensalada_cesar_con_pollo":
        return preparar_ensalada_cesar_con_pollo()
    elif receta == "wrap_de_pollo":
        return preparar_wrap_pollo()
    elif receta == "sandwich_clasico":
        return preparar_sandwich_clasico()
    else:
        return {"error": "Receta no encontrada"}

# Ejemplo de uso
receta_elegida = "wrap_de_pollo"
receta = emplatado(receta_elegida)

# Imprimir los pasos de la receta
for paso in receta["pasos"]:
    print(paso)
