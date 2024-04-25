class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def imprimir_arbol(nodo, espacio=""):
    if nodo is None:
        return
    
    imprimir_arbol(nodo.derecha, espacio + "   ")
    print(espacio + "|--", nodo.valor)
    imprimir_arbol(nodo.izquierda, espacio + "   ")

# Ejemplo de uso
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)

print("Árbol binario:")
imprimir_arbol(raiz)
