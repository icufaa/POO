class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self,dato):
        self.raiz = Nodo(dato)

    #Funcion (Recibe el nodo y el dato que se va a agregar)
    def __agregar_recursivo(self, nodo, dato):
        #Si el dato o valor es menor que el dato que ya tiene el nodo
        if dato < nodo.dato:
            #y ademas si el nodo esta disponible a su izquierda
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)

    #Metodos de recorrido para el arbol

    # En Inorden Primero se visita toda la izquierda, se imprime el actual y despues se visita la derecha
    def __inorden_recursivo(self,nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    # En Preorden se visita primero el actual, despues la izquierda y despues la derecha
    def __preorden_recursivo(self,nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self,nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.dato, end=", ")

    #Metodo buscar dentro del arbol binario

    def __buscar(self,nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)
        
    # Funciones publicas

    #En agregar solo recibe un dato y se invoca recursivo pero desde la raiz
    def agregar(self,dato):
        self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        print("Arbol Inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")
    
    def preorden(self):
        print("Arbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")
    
    def postorden(self):
        print("Arbol Postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")
    
    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)
    


arbol = Arbol("Pepe")
arbol.agregar("Sand")
arbol.agregar("Chabona")
arbol.agregar("Milei")
arbol.agregar("Jorge")
arbol.agregar("Messi")
arbol.agregar("Harry")


nombre = input("Ingresa algo para agregar al arbol: ")
arbol.agregar(nombre)
arbol.preorden()
arbol.inorden()
arbol.postorden()

#Busqueda

busqueda= input("Busca algo en el arbol: ")
nodo = arbol.buscar(busqueda)

if nodo is None:
    print(f'{busqueda} No existe')
else:
    print(f"{busqueda} si existe")
