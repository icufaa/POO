import random
import time

def generar_array(tamano, rango):
    return [random.randint(0, rango) for _ in range(tamano)]

def ordenar_array(array):
    return sorted(array)

def encontrar_maximo(array):
    maximo = array[0]
    for numero in array:
        if numero > maximo:
            maximo = numero
    return maximo

def encontrar_minimo(array):
    minimo = array[0]
    for numero in array:
        if numero < minimo:
            minimo = numero
    return minimo

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
        print("1. Buscar el número máximo en el array")
        print("2. Buscar el número mínimo en el array")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            maximo = encontrar_maximo(array_ordenado)
            print(f"El número máximo en el array es: {maximo}")
        elif opcion == '2':
            minimo = encontrar_minimo(array_ordenado)
            print(f"El número mínimo en el array es: {minimo}")
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
