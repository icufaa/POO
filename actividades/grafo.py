import queue  # Importa el módulo queue para usar la cola de prioridad en el algoritmo de Dijkstra

class Nodo:
    def __init__(self, info):
        self.info = info  # Información contenida en el nodo
        self.visitado = False  # Marca si el nodo ha sido visitado
        self.etiqueta = 0  # Etiqueta del nodo, no se utiliza en este código
        self.ady = dict()  # Diccionario de nodos adyacentes
        self.peso_ady = dict()  # Diccionario de pesos de los arcos hacia los nodos adyacentes

    def __eq__(self, other):
        if other is Nodo:
            return self.info == other.info  # Compara dos nodos por su información
        return False

    def __lt__(self, other):
        if other is Nodo:
            return self.info < other.info  # Compara si un nodo es menor que otro por su información
        return False

    def __hash__(self):
        return hash(self.info)  # Permite que el nodo sea usado como clave en un diccionario

class Grafo:
    def __init__(self):
        self.dic_nodos = dict()  # Diccionario de nodos del grafo
        self.lista_nodos = list()  # Lista de nodos del grafo
        self.cantidad_arcos = 0  # Contador de arcos en el grafo

    def esta_vacio(self):
        return len(self.lista_nodos) == 0  # Devuelve True si el grafo está vacío

    def agregar_vertice(self, vertice):
        if vertice not in self.dic_nodos:
            nodo = Nodo(vertice)  # Crea un nuevo nodo
            self.lista_nodos.append(nodo)  # Añade el nodo a la lista de nodos
            self.dic_nodos[vertice] = nodo  # Añade el nodo al diccionario de nodos

    def eliminar_vertice(self, vertice):
        if vertice in self.dic_nodos:
            nodo_v = self.dic_nodos[vertice]
            self.lista_nodos.remove(nodo_v)  # Elimina el nodo de la lista de nodos
            del self.dic_nodos[vertice]  # Elimina el nodo del diccionario de nodos
            for nodo in self.lista_nodos:
                if vertice in nodo.ady:
                    del nodo.ady[vertice]  # Elimina el nodo de la lista de adyacencia de los demás nodos
                    del nodo.peso_ady[vertice]  # Elimina el peso asociado al arco

    def agregar_arco(self, alfa, beta, peso):
        if beta != alfa and alfa in self.dic_nodos and beta in self.dic_nodos:
            nodo_a = self.dic_nodos[alfa]
            nodo_b = self.dic_nodos[beta]
            if beta not in nodo_a.ady:
                nodo_a.ady[beta] = nodo_b  # Añade el nodo beta a la lista de adyacencia de alfa
                nodo_a.peso_ady[beta] = peso  # Añade el peso del arco
                self.cantidad_arcos += 1  # Incrementa el contador de arcos

    def eliminar_arco(self, alfa, beta):
        if beta != alfa and alfa in self.dic_nodos and beta in self.dic_nodos:
            nodo_a = self.dic_nodos[alfa]
            del nodo_a.ady[beta]  # Elimina el nodo beta de la lista de adyacencia de alfa
            del nodo_a.peso_ady[beta]  # Elimina el peso del arco
            self.cantidad_arcos -= 1  # Decrementa el contador de arcos

    def contar_arcos(self):
        return self.cantidad_arcos  # Devuelve la cantidad de arcos en el grafo

    def obtener_peso_arco(self, alfa, beta):
        if alfa in self.dic_nodos:
            nodo_a = self.dic_nodos[alfa]
            if beta in nodo_a.peso_ady:
                return nodo_a.peso_ady[beta]  # Devuelve el peso del arco entre alfa y beta

    def obtener_vecinos(self, alfa):
        if alfa in self.dic_nodos:
            nodo_a = self.dic_nodos[alfa]
            return nodo_a.ady.keys()  # Devuelve los nodos adyacentes a alfa

    def contar_vertices(self):
        return len(self.lista_nodos)  # Devuelve la cantidad de nodos en el grafo

    def limpiar_marcas(self):
        for nodo in self.lista_nodos:
            nodo.visitado = False  # Marca todos los nodos como no visitados

    def algo_DFS(self, alfa):
        self.limpiar_marcas()
        lista_dfs = list()  # Lista para almacenar el recorrido DFS
        por_visitar = list()  # Pila para gestionar los nodos por visitar
        if alfa in self.dic_nodos:
            nodo_a = self.dic_nodos[alfa]
            por_visitar.append(nodo_a)
            while len(por_visitar) > 0:
                nodo = por_visitar.pop()
                if nodo.visitado:
                    continue
                nodo.visitado = True
                lista_dfs.append(nodo.info)  # Añade la información del nodo a la lista DFS
                for nodo2 in nodo.ady.values():
                    por_visitar.append(nodo2)  # Añade los nodos adyacentes a la pila
        return lista_dfs  # Devuelve la lista del recorrido DFS

    def algo_BFS(self, alfa):
        self.limpiar_marcas()
        lista_bfs = list()  # Lista para almacenar el recorrido BFS
        por_visitar = list()  # Cola para gestionar los nodos por visitar
        if alfa in self.dic_nodos:
            nodo_a = self.dic_nodos[alfa]
            por_visitar.append(nodo_a)
            while len(por_visitar) > 0:
                nodo = por_visitar.pop(0)
                if nodo.visitado:
                    continue
                nodo.visitado = True
                lista_bfs.append(nodo.info)  # Añade la información del nodo a la lista BFS
                for nodo2 in nodo.ady.values():
                    por_visitar.append(nodo2)  # Añade los nodos adyacentes a la cola
        return lista_bfs  # Devuelve la lista del recorrido BFS

    def es_camino(self, alfa, beta):
        dfs = self.algo_DFS(alfa)
        if beta in dfs:
            return True  # Devuelve True si hay un camino de alfa a beta
        return False

    def algo_Dijkstra(self, alfa):
        if alfa not in self.dic_nodos:
            return dict()  # Devuelve un diccionario vacío si alfa no está en el grafo

        nodo_a = self.dic_nodos[alfa]
        self.limpiar_marcas()
        distancia = dict()  # Diccionario para almacenar la distancia mínima desde alfa
        visitados = list()  # Lista de nodos visitados
        distancia[alfa] = 0  # La distancia desde alfa a sí mismo es 0
        nodo_a.visitado = True
        visitados.append(nodo_a)
        pq = queue.PriorityQueue()
        for nodo in nodo_a.ady.values():
            pq.put((nodo_a.peso_ady[nodo.info], nodo))  # Añade los nodos adyacentes a la cola de prioridad
        while not pq.empty():
            costo, nodo = pq.get()
            if nodo.visitado:
                continue
            nodo.visitado = True
            distancia[nodo.info] = costo  # Establece la distancia mínima al nodo

            for nd in nodo.ady.values():
                pq.put((nodo.peso_ady[nd.info] + costo, nd))  # Actualiza la cola de prioridad con los nodos adyacentes

        return distancia  # Devuelve el diccionario de distancias

# Creación del grafo y adición de vértices y arcos
g = Grafo()
g.agregar_vertice(1)
g.agregar_vertice(2)
g.agregar_vertice(3)
g.agregar_vertice(4)
g.agregar_vertice(5)
g.agregar_vertice(6)
g.agregar_arco(4, 5, 1)
g.agregar_arco(5, 2, 122)
g.agregar_arco(2, 1, 1)
g.agregar_arco(1, 3, 1)
g.agregar_arco(3, 1, 221)
g.agregar_arco(5, 1, 2131)
g.agregar_arco(4, 5, 1)  # Arco duplicado, podría ser redundante
g.agregar_arco(3, 4, 1)
g.agregar_arco(3,1,23)
g.agregar_arco(1,3,23323)
g.agregar_arco(6,1,223)


# Ejecución del algoritmo de Dijkstra desde el nodo 1
l = g.algo_Dijkstra(1)
print(l)
l = g.algo_Dijkstra(5)
print(l)
l = g.algo_Dijkstra(2)
print(l)
l = g.algo_Dijkstra(6)
print(l)  # Imprime el resultado de las distancias mínimas desde el nodo 1



