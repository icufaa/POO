class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class LinkedList:
    def __init__(self):
        self.head = None

    
    def insertar_nodo_al_inicio(self,dato):
        nuevo_nodo = Nodo(dato)
        #Si la cabecera esta vacia, inserta el nodo en la cabecera
        if self.head is None:
            self.head = nuevo_nodo
            return
        nuevo_nodo.siguiente = self.head
        self.head = nuevo_nodo
    

    def insetar_nodo_al_final (self,dato):
        nuevo_nodo = Nodo(dato)
        if self.head is None:
            self.head = nuevo_nodo
            return
        actual = self.head
        while (actual.siguiente):
            actual = actual.siguiente
        
        actual.siguiente = nuevo_nodo

    def print_linked_list(self):
        actual = self.head
        while (actual):
            print(actual.dato, "->", end=" ")
            actual = actual.siguiente

mi_lista=LinkedList()
mi_lista.insertar_nodo_al_inicio(5)
mi_lista.insertar_nodo_al_inicio(4)
mi_lista.insertar_nodo_al_inicio(3)
mi_lista.insertar_nodo_al_inicio(2)
mi_lista.insertar_nodo_al_inicio(10)
mi_lista.insertar_nodo_al_inicio(25)
mi_lista.insetar_nodo_al_final(25)
mi_lista.insetar_nodo_al_final(15)
mi_lista.insetar_nodo_al_final(12)
mi_lista.print_linked_list()
