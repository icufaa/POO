import os
import csv
import time

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

    def inorden(self, nodo, nivel=0, prefijo="Raiz: "):
        if nodo is not None:
            self.inorden(nodo.izquierda, nivel + 1, "\t\tIzq---: ")
            print(" " * (nivel * 4) + prefijo + str(nodo.dato))
            self.inorden(nodo.derecha, nivel + 1, "\t\tDer---: ")

    def preorden(self, nodo, nivel=0, prefijo="Raiz: "):
        if nodo is not None:
            print(" " * (nivel * 4) + prefijo + str(nodo.dato))
            self.preorden(nodo.izquierda, nivel + 1, "\t\tIzq---: ")
            self.preorden(nodo.derecha, nivel + 1, "\t\tDer---: ")

    def postorden(self, nodo, nivel=0, prefijo="Raiz: "):
        if nodo is not None:
            self.postorden(nodo.izquierda, nivel + 1, "\t\tIzq---: ")
            self.postorden(nodo.derecha, nivel + 1, "\t\tDer---: ")
            print(" " * (nivel * 4) + prefijo + str(nodo.dato))

    def buscar_dfs(self, dato):
        return self.__buscar_dfs_recursivo(self.raiz, dato)
    
    def __buscar_dfs_recursivo(self, nodo, dato):
        if nodo is None:
            return None
        if nodo.dato == dato:
            return nodo
        print(f"Buscando en nodo: {nodo.dato}")
        resultado_izquierda = self.__buscar_dfs_recursivo(nodo.izquierda, dato)
        if resultado_izquierda is not None:
            return resultado_izquierda
        return self.__buscar_dfs_recursivo(nodo.derecha, dato)
    
    def buscar_bfs(self, dato):
        if self.raiz is None:
            return None
        cola = [self.raiz]
        while cola:
            nodo = cola.pop(0)
            print(f'Buscando en nodo: {nodo.dato}')
            if nodo.dato == dato:
                return nodo
            if nodo.izquierda is not None:
                cola.append(nodo.izquierda)
            if nodo.derecha is not None:
                cola.append(nodo.derecha)
        return None
    
    def altura(self,nodo):
        if nodo is None:
            return 0
        altura_izquierda = self.altura(nodo.izquierda)
        altura_derecha = self.altura(nodo.derecha)
        return max(altura_izquierda, altura_derecha) + 1
    
    def peso(self,nodo):
        if nodo is None:
            return  0
        return self.peso(nodo.izquierda) + self.peso(nodo.derecha) + 1

def cargar_datos():
    arbol = Arbol()
    
    current_directory = os.getcwd()
    print(f"Directorio actual: {current_directory}")

    relative_file_path = 'actividades/MOCK_DATA.csv'

    if os.path.exists(relative_file_path):
        file_path = relative_file_path
    else:
        file_path = os.path.join(current_directory, 'actividades', 'MOCK_DATA.csv')
        if not os.path.exists(file_path):
            print(f"El archivo {file_path} no existe.")
            return None

    try:
        with open(file_path, mode='r', encoding='utf-8', newline='') as archivo:
            lector_csv = csv.reader(archivo)
            next(lector_csv)  # Saltar la cabecera
            for i, fila in enumerate(lector_csv):
                if len(fila) < 2:
                    print(f"Fila {i} está incompleta: {fila}")
                    continue
                apellido = fila[1]
                arbol.agregar(apellido)
        return arbol
    except Exception as e:
        print(f"Se produjo un error al leer el archivo: {e}")
        return None

def agregar_persona_manual(arbol,file_path):
    firts_name = input("Nombre de la persona: ")
    last_name = input(f"Apellido de {firts_name}: ")
    while True:
        flag_genero = int(input("Elegi el Genero Pibe\n[1]Male [2]Female\nOpcion:"))
        if flag_genero == 1:
            genero = "Male"
            break
        elif flag_genero == 2:
            genero = "Female"
            break
        else:
            print("Gennero Invalido, intente nuevamente...")
        
    ciudad = input(f"Ciudad de {firts_name}: ")
    pais = input(f"País de {firts_name}: ")

    #Agregar al arbol 
    arbol.agregar(last_name.capitalize())

    #Agregar al csv
    try:
        with open(file_path, mode="a",encoding="utf-8",newline="") as archivo:
            escritor_csv = csv.writer(archivo)
            escritor_csv.writerow([firts_name,last_name,genero,ciudad,pais])
        print(f"""Persona Agregada Con Exito\n-------------------------- \nNombre:{firts_name}\nApellido:{last_name}\nGenero:{genero}\nCiudad:{ciudad}\nPais:{pais}\n\n\n""")
    except Exception as e:
        print(f"Se Produjo un error al escribir en el archivo CSV: {e}")


def salir():
    print("Saliendo del programa.")
    exit()

def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    elif os.name == 'nt':
        _ = os.system('cls')

def menu(arbol,file_path):
    clear()
    while True:
        print("1. Imprimir Recorrido Inorden")
        print("2. Imprimir Recorrido Preorden")
        print("3. Imprimir Recorrido Postorden")
        print("4. Buscar Persona por (DFS)")
        print("5. Buscar Persona por (BFS)")
        print("6. Insetar Persona manualmente ")
        print("7. Imprimir Altura del Arbol")
        print("8. Imprimir Peso del Arbol")
        print("9. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            clear()
            print("Recorrido Inorden:")
            inicio = time.time()
            arbol.inorden(arbol.raiz)
            fin = time.time()
            tiempo_total = fin - inicio
            print(f"\nTiempo que tardo en ejecutar el recorrido: {tiempo_total:.5f} segundos\n\n")
        elif opcion == "2":
            clear()
            print("\nRecorrido Preorden:")
            inicio = time.time()
            arbol.preorden(arbol.raiz)
            fin = time.time()
            tiempo_total = fin - inicio
            print(f"\nTiempo que tardo en ejecutar el recorrido: {tiempo_total:.5f} segundos\n\n")
        elif opcion == "3":
            clear()
            print("\nRecorrido Postorden:")
            inicio = time.time()
            arbol.postorden(arbol.raiz)
            fin = time.time()
            tiempo_total = fin - inicio
            print(f"\nTiempo que tardo en ejecutar el recorrido: {tiempo_total:.5f} segundos\n\n")
        elif opcion == "4":
            clear()
            dato = input("Ingresa el apellido a buscar por (DFS): ")
            inicio = time.time()
            resultado = arbol.buscar_dfs(dato.capitalize())
            fin = time.time()
            if resultado:
                print(f"Persona encontrada: {resultado.dato}")
            else:
                print("Persona no encontrada")
            tiempo_total = fin - inicio
            print(f"\nTiempo que tardo en ejecutar la busqueda: {tiempo_total:.5f} segundos\n\n")
        elif opcion == "5":
            clear()
            dato = input("Ingrese el apellido a buscar (BFS): ")
            inicio = time.time()
            resultado = arbol.buscar_bfs(dato.capitalize())
            fin = time.time()
            if resultado:
                print(f"Persona encontrada: {resultado.dato}")
            else:
                print("Persona no encontrada")
            tiempo_total = fin - inicio
            print(f"\nTiempo que tardo en ejecutar la búsqueda: {tiempo_total:.5f} segundos\n\n")
        elif opcion == "6":
            clear()
            agregar_persona_manual(arbol,file_path)
        elif opcion == "7":
            clear()
            inicio = time.time()
            altura = arbol.altura(arbol.raiz)
            fin = time.time()
            print(f"la altura del arbol es de: {altura}")
            tiempo_total = fin - inicio
            print(f"\nTiempo que tardo en calcular la altura del arbol es de: {tiempo_total:.5f}\n\n")
        elif opcion == "8":
            clear()
            inicio = time.time()
            peso = arbol.peso(arbol.raiz)
            fin= time.time()
            print(f"El peso del arbol es de: {peso}")
            tiempo_total = fin - inicio
            print(f"\nTiempo que tardo en calcular el peso del arbol es de: {tiempo_total:.5f}\n\n")
        elif opcion == "9":
            clear()
            print("Saliendo del sistema...")
            salir()
        else:
            print("Opción inválida. Inténtalo de nuevo.")

# Cargar datos del repositorio y ejecutar el menú
if __name__ == "__main__":
    arbol = cargar_datos()
    if arbol is not None:
        file_path = os.path.join(os.getcwd(),"actividades","MOCK_DATA.csv")
        menu(arbol,file_path)
    else:
        print("No se pudieron cargar los archivos csv")
