from itertools import product

#Toma de datos
def ingresar_anos_nacimiento():
    cantidad = int(input("Ingrese la cantidad de integrantes: "))
    anios = [int(input(f"Ingrese el año de nacimiento del integrante {i+1}: ")) for i in range(cantidad)]
    return anios

#Analicis de datos

def cant_pares(list):
    return sum(1 for anio in list if anio % 2 == 0)

def cant_impares(list):
    return sum(1 for anio in list if anio % 2 != 0)

def nacidos_2000(list):
    if all(ano > 2000 for ano in list):
        return "Grupo Z"
    return "Otros grupos"

def es_bisiesto_mensaje(list):
    if any(es_bisiesto(anio) for anio in list):
        return "Tenemos un año especial"
    return "No tenemos año especial"

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def producto_cartesiano(anos):
    edades = [2025 - ano for ano in anos]
    producto = list(product(anos, edades))
    return producto
