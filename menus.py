from operaciones_dni import *
from operaciones_anios import *

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*40)
    print("         MENÚ PRINCIPAL")
    print("="*40)
    print("1- **Operaciones con DNIs**")
    print("2- **Operaciones con años de nacimiento**")
    print("3- Salir")
    print("="*40)

def operaciones_dni():
    print("\n" + "="*50)
    print("🆔           OPERACIONES CON DNIs           🆔")
    print("="*50)
    
    conjunto = ingresar_dnis()
    
    print("\n" + "▪"*50)
    print("📊                RESULTADOS               📊")
    print("▪"*50)
    
    print(f"\n🔗 Unión de los conjuntos:")
    print(f"   {operacion_conjuntos_union(conjunto)}")
    
    print(f"\n🔄 Intersección de los conjuntos:")
    print(f"   {operacion_conjuntos_interseccion(conjunto)}")
    
    print(f"\n⚖️  Diferencias entre pares A - B:")
    print(f"   {operacion_conjuntos_diferencia_pares_ab(conjunto)}")

    print(f"\n⚖️  Diferencias entre pares B - A:")
    print(f"   {operacion_conjuntos_diferencia_pares_ba(conjunto)}")
    
    print(f"\n🔀 Diferencia simétrica:")
    print(f"   {operacion_conjuntos_diferencia_simetrica(conjunto)}")

    print(f"\n🔍 Evaluación de condiciones:")
    print(f"   {evaluar_condiciones(conjunto)}")

    print("\n" + "="*50)
    input("✨ Presiona Enter para volver al menú principal...")
    print("="*50)

def operaciones_años():
    """Función para manejar operaciones con años de nacimiento"""
    print("\n" + "="*55)
    print("🎂        OPERACIONES CON AÑOS DE NACIMIENTO        🎂")
    print("="*55)
    
    lista_anios = ingresar_anos_nacimiento()
    
    print("\n" + "▪"*55)
    print("📈                   ESTADÍSTICAS                  📈")
    print("▪"*55)
    
    print(f"\n🔢 Cantidad de años pares:")
    print(f"   {cant_pares(lista_anios)}")
    
    print(f"\n🔢 Cantidad de años impares:")
    print(f"   {cant_impares(lista_anios)}")
    
    print(f"\n🎯 Análisis de nacidos después del 2000: {nacidos_2000(lista_anios)}")
    
    print(f"\n📅 Evaluación de años bisiestos: {es_bisiesto_mensaje(lista_anios)}")

    print(f"\n🔗 Producto cartesiano: {producto_cartesiano(lista_anios)}")
    

    print("\n" + "="*55)
    input("✨ Presiona Enter para volver al menú principal...")
    print("="*55)

def menuPrincipal():
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSelecciona una opción (1-3): ").strip()
            
            if opcion == "1":
                operaciones_dni()
            elif opcion == "2":
                operaciones_años()
            elif opcion == "3":
                print("\n¡Gracias por usar el programa! 👋")
                break
            else:
                print("\n❌ Opción no válida. Por favor, selecciona 1, 2 o 3.")
                input("Presiona Enter para continuar...")
                
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido por el usuario!")
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            input("Presiona Enter para continuar...")