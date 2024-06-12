import random
import time

def generar_array(tamano, rango):
    return [random.randint(0, rango) for _ in range(tamano)]

def ordenar_array(array):
    return sorted(array)

def busqueda_binaria(array, numero):
    izquierda, derecha = 0, len(array) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if array[medio] == numero:
            return medio
        elif array[medio] < numero:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def main():
    tamano = 100
    rango = 1000
    
    # Generar array
    array = generar_array(tamano, rango)
    print("Array desordenado:")
    print(array)
    
    # Medir tiempo de inicio
    inicio = time.time() * 1000
    
    # Ordenar array
    array_ordenado = ordenar_array(array)
    
    # Medir tiempo de fin
    fin = time.time() * 1000
    
    print("\nArray ordenado:")
    print(array_ordenado)
    
    print("\nTiempo de inicio del ordenamiento (ms):", inicio)
    print("Tiempo de finalización del ordenamiento (ms):", fin)
    print("Tiempo total de ordenamiento (ms):", fin - inicio)
    
    while True:
        print("\nMenú:")
        print("1. Buscar un número en el array")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            numero = int(input("Introduce el número a buscar: "))
            indice = busqueda_binaria(array_ordenado, numero)
            if indice != -1:
                print(f"El número {numero} se encuentra en el índice {indice}.")
            else:
                print(f"El número {numero} no se encuentra en el array.")
        elif opcion == '2':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
