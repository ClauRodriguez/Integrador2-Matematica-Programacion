#Toma de datos
def ingresar_dnis():
    cantidad = int(input("Ingrese la cantidad de integrantes: "))
    # crea una lista con los dni de cada integrante
    dnis = [input(f"Ingrese el DNI del integrante {i+1}: ") for i in range(cantidad)]
    conjuntos = [obtener_conjunto_dni(dni) for dni in dnis]
    return conjuntos

#Operaciones con conjuntos
def obtener_conjunto_dni(dni):
    return set(str(dni))

def operacion_conjuntos_union(conjuntos):
    return sorted(set.union(*conjuntos))

def operacion_conjuntos_interseccion(conjuntos):
    return sorted(set.intersection(*conjuntos))

def operacion_conjuntos_diferencia_pares_ba(conjuntos):
    return [sorted(conjuntos[i] - conjuntos[i+1]) for i in range(len(conjuntos)-1)]

def operacion_conjuntos_diferencia_pares_ab(conjuntos):
    return [sorted(conjuntos[i+1] - conjuntos[i]) for i in range(len(conjuntos)-1)]

def operacion_conjuntos_diferencia_simetrica(conjuntos):
    return sorted(list(set.symmetric_difference(*conjuntos)))


# Expresiones Lógicas
def evaluar_condiciones(conjuntos):
    mensajes = []
    
    if all(len(conjunto) > 5 for conjunto in conjuntos):
        mensajes.append("Se encontró Alta diversidad numérica")
    
    if any(digito in conjunto for conjunto in conjuntos for digito in set.intersection(*conjuntos)):
        mensajes.append("Se encontró al menos un Dígito común")
    
    return "\n".join(mensajes)