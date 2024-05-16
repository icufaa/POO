import csv

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol: 
    def __init__(self):
        self.raiz = None

    def agregar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self.__agregar_recursivo(self.raiz, dato)

    def __agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)

    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izquierda)
            print(nodo.dato, end=" ")
            self.inorden(nodo.derecha)

    def preorden(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=" ")
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    def postorden(self, nodo):
        if nodo is not None:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.dato, end=" ")

# Crear el árbol
arbol = Arbol()

# Abrir el archivo CSV y agregar los datos al árbol
with open('C:\\Users\\Usuario\\Documents\\actividades\\POO\\MOCK_DATA.csv', 'r') as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        # Suponiendo que la columna deseada es la primera
        dato = fila[2]
        arbol.agregar(dato)


def salir():
    print("Saliendo del programa.")
    exit()


def menu():
    while True:
        print("1. Imprimir Recorrido Inorden")
        print("2. Imprimir Recorrido Preorden")
        print("3. Imprimir Recorrido Postorden")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            print("Recorrido Inorden:")
            arbol.inorden(arbol.raiz)
        elif opcion == "2":
            print("\nRecorrido Preorden:")
            arbol.preorden(arbol.raiz)
        elif opcion == "3":
            print("\nRecorrido Postorden:")
            arbol.postorden(arbol.raiz)
        elif opcion == "4":
            salir()
        else:
            print("Opción inválida. Inténtalo de nuevo.")
