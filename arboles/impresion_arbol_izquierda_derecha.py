class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self, valor_raiz):
        self.raiz = Nodo(valor_raiz)

    def agregar_nodo(self, valor, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz
        if valor <= nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self.agregar_nodo(valor, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self.agregar_nodo(valor, nodo_actual.derecha)

    def buscar(self, valor, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual
        if valor < nodo_actual.valor:
            return self.buscar(valor, nodo_actual.izquierda)
        return self.buscar(valor, nodo_actual.derecha)

    def imprimir_arbol(self, raiz, nivel=0, prefijo=''):
        if raiz is not None:
            print(' ' * (nivel * 4) + prefijo + str(raiz.valor))
            if raiz.izquierda is not None or raiz.derecha is not None:
                self.imprimir_arbol(raiz.izquierda, nivel + 1, 'I:')
                self.imprimir_arbol(raiz.derecha, nivel + 1, 'D:')

# Ejemplo de uso
arbol = ArbolBinario(10)
arbol.agregar_nodo(5)
arbol.agregar_nodo(15)
arbol.agregar_nodo(3)
arbol.agregar_nodo(7)
arbol.agregar_nodo(12)
arbol.agregar_nodo(17)

# Búsqueda de un valor
nodo_buscado = arbol.buscar(7)
if nodo_buscado:
    print("Valor encontrado:", nodo_buscado.valor)
else:
    print("Valor no encontrado")

# Imprimir el árbol
print("\nÁrbol binario:")
arbol.imprimir_arbol(arbol.raiz)
