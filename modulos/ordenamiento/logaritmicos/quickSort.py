import random
import time

def generar_array(tamano, rango):
    return [random.randint(0, rango) for _ in range(tamano)]

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def crear_tabla_hash(array):
    tabla_hash = {}
    for indice, valor in enumerate(array):
        tabla_hash[valor] = indice
    return tabla_hash

def buscar_en_tabla_hash(tabla_hash, numero):
    return tabla_hash.get(numero, -1)

def main():
    tamano = 100
    rango = 1000
    
    # Generar array
    array = generar_array(tamano, rango)
    print("Array desordenado:")
    print(array)
    
    # Medir tiempo de inicio
    inicio = time.time() * 1000
    
    # Ordenar array con quick sort
    array_ordenado = quick_sort(array)
    
    # Crear tabla hash
    tabla_hash = crear_tabla_hash(array_ordenado)
    
    # Medir tiempo de fin
    fin = time.time() * 1000
    
    print("\nArray ordenado:")
    print(array_ordenado)
    
    print("\nTiempo de inicio del ordenamiento (ms):", inicio)
    print("Tiempo de finalización del ordenamiento (ms):", fin)
    print("Tiempo total de ordenamiento (ms):", fin - inicio)
    
    while True:
        print("\nMenú:")
        print("1. Buscar un número en el array utilizando la tabla hash")
        print("2. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            numero = int(input("Introduce el número a buscar: "))
            indice = buscar_en_tabla_hash(tabla_hash, numero)
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
