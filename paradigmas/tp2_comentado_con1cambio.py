# TRABAJO PRACTICO N2 -
# MEYER IVÁN - VIÑALES FACUNDO
#prueba 2 cometarios blabla

# Importación de módulos necesarios
import random  # Para generar números aleatorios
import os  # Para interactuar con el sistema operativo

# Lista de seguimiento de carritos y cantidad de carritos disponibles inicialmente
seguimientoCarritos = []
carritosDisponibles = 0

# Diccionario que asocia números de condiciones con sus descripciones
diccionarioCondiciones = {
    1: "NORMAL",
    2: "DISCAPACITADO",
    3: "EMBARAZADA",
    4: "ANCIANO",
}

# Lista de nombres de clientes
lista_clientes = [
    "Juan", "María", "Pedro", "Ana", "Luis", "Sofía", "Carlos", "Laura", "Miguel", "Isabel",
    "Alejandro", "Lucía", "Javier", "Elena", "Diego", "Carmen", "Jorge", "Teresa", "Roberto", "Paula",
    "José", "Silvia", "Fernando", "Raquel", "Andrés", "Natalia", "Antonio", "Patricia", "Rafael", "Eva",
    "Francisco", "Marina", "Pablo", "Beatriz", "David", "Adriana", "Daniel", "Clara", "Joaquín", "Nuria",
    "Manuel", "Sara", "Ángel", "Cristina", "Ricardo", "Verónica", "Alberto", "Inés", "Guillermo", "Victoria"
]


# Clase para representar un carrito
class Carrito():
    def __init__(self) -> None:
        global carritosDisponibles
        carritosDisponibles += 1
        self.propietario = None  # Dueño del carrito
        self.cola = None  # Fila en la que se encuentra el carrito
        self.id = carritosDisponibles  # Identificador único del carrito


# Clase para representar a una persona (cliente)
class Persona():
    def __init__(self, condicion):
        self.condicion = condicion  # Condición de la persona (1: Normal, 2: Discapacitado, 3: Embarazada, 4: Anciano)
        self.representacion = diccionarioCondiciones[condicion][0]  # Representación de la condición (N, D, E, A)
        self.nombre = random.choice(lista_clientes)  # Nombre aleatorio de la persona

    @property
    def condicion(self):
        return self._condicion

    @condicion.setter
    def condicion(self, value):
        if value in list(diccionarioCondiciones.keys()):
            self._condicion = value
        else:
            raise ValueError("Condicion ingresada no válida")


# Clase para representar un nodo en una estructura de datos enlazada
class Nodo:
    def __init__(self, data):
        self.data = data  # Datos almacenados en el nodo
        self.next = None  # Referencia al siguiente nodo


# Clase para representar una pila (estructura de datos LIFO)
class Pila:
    def __init__(self):
        self.tope = None  # Nodo superior de la pila
        self.count = 0  # Contador de elementos en la pila

    # Método para agregar un elemento a la pila
    def agregarAPila(self, item):
        nodoitem = Nodo(item)
        if self.tope is None:
            self.tope = nodoitem
            self.count += 1
        else:
            nodoitem.next = self.tope
            self.tope = nodoitem
            self.count += 1

    # Método para sacar un elemento de la pila
    def sacardePila(self):
        if self.tope is None:
            return None
        else:
            viejoTope = self.tope.data
            nuevoTope = self.tope.next
            self.tope.next = None
            self.tope = nuevoTope
            self.count -= 1
            return viejoTope

    # Método para verificar si un elemento está en la pila
    def estaEnPila(self, value):
        localcount = 0
        actual = self.tope
        while localcount < self.count:
            if actual.data == value:
                return True
            actual = actual.next
            localcount += 1
        return False


# Clase para representar una cola (estructura de datos FIFO)
class Queue:
    def __init__(self):
        self.final = None  # Nodo final de la cola
        self.frente = None  # Nodo frontal de la cola
        self.count = 0  # Contador de elementos en la cola

    # Método para sacar un elemento de la cola
    def sacarDeCola(self):
        if self.frente is None:
            print('Cola vacia')
        actual = self.frente
        self.frente = self.frente.next
        if self.frente is None:
            self.final = None
        self.count -= 1
        return actual.data

    # Método para agregar un elemento a la cola
    def agregarACola(self, item):
        nodo = Nodo(item)

        if self.frente is None:
            self.frente = nodo
            self.final = nodo
        else:
            self.final.next = nodo
            self.final = nodo
        self.count += 1

    # Función que puede retornar o eliminar un elemento mediante un índice
    def retornarElemento(self, argindex):
        localIndex = 0
        actual = self.frente
        while actual.next is not None or argindex < self.count:
            if argindex == localIndex:
                return actual.data
            else:
                actual = actual.next
                localIndex += 1
        print("Indice de elemento no existe")

    # Método para verificar si la cola está vacía
    def isEmpty(self):
        return self.final is None and self.frente is None

    # Método para obtener el tamaño de la cola
    def size(self):
        return self.count


# Función para mostrar gráficamente el estado de la tienda
def displayEstadoGeneral():
    pilaCarritosString = str()
    carritosDisponiblesString = "[CARRITOS]"
    for i in range(pilaCarritosDisponibles.count):
        carritosDisponiblesString += "\U0001f6d2 "
    try:
        for i in range(filaCarritos.count):
            pilaCarritosString += filaCarritos.retornarElemento(i).representacion
    except:
        None
    print(carritosDisponiblesString + "\t" + pilaCarritosString )

    filaCajaNormalString = "\n[CAJA N]\t"
    filaCajaDiscapString = "\n[CAJA D]\t"
    filacajaEmbAncString = "\n[CAJA E/A]\t"

    for i in range(filaCajaNormal.size()):
        filaCajaNormalString += filaCajaNormal.retornarElemento(i).representacion + " - "
    for i in range(filaCajaDiscap.size()):
        filaCajaDiscapString += filaCajaDiscap.retornarElemento(i).representacion + " - "
    for i in range(filaCajaEmbAnc.size()):
        filacajaEmbAncString += filaCajaEmbAnc.retornarElemento(i).representacion + " - "

    print(filaCajaNormalString)
    print(filaCajaDiscapString)
    print(filacajaEmbAncString)


# Función para mostrar el estado de los carritos
def displayCarritos():
    for i in range(len(seguimientoCarritos)):
        carritoActual = seguimientoCarritos[i]
        propietario = carritoActual.propietario
        ubicacion = carritoActual.cola

        if propietario == None:
            ubicacion = "Pila de carritos"
        if carritoActual.cola == filaCajaNormal:
            ubicacion = "Fila de personas normales"
        elif carritoActual.cola == filaCajaDiscap:
            ubicacion = "Fila de personas discapacitadas"
        elif carritoActual.cola == filaCajaEmbAnc:
            ubicacion = "Fila de personas embarazadas / ancianas"

        try:
            print(
                f"Estado de carrito {carritoActual.id}\nPropietario = {propietario.nombre} ({diccionarioCondiciones[propietario.condicion].lower()})\nUbicacion = {ubicacion}\n")
        except:
            print(f"Estado de carrito {carritoActual.id}\nPropietario = Nadie\nUbicacion = {ubicacion}\n")

# Función para determinar a que fila de caja debe ir un cliente según su condición
def prioridadColaCaja(clientearg):
    condicionVal = diccionarioCondiciones[clientearg.condicion]
    # Si es normal, se fija si las demás filas estan vacias y se mete si es asi
    if condicionVal == diccionarioCondiciones[1]:
        if filaCajaNormal.isEmpty():
            return filaCajaNormal
        if filaCajaDiscap.isEmpty():
            return filaCajaDiscap
        if filaCajaEmbAnc.isEmpty():
            return filaCajaEmbAnc
        return filaCajaNormal
    # Mismo caso para los discapacitados
    elif condicionVal == diccionarioCondiciones[2]:
        if filaCajaDiscap.isEmpty():
            return filaCajaDiscap
        if filaCajaNormal.isEmpty():
            return filaCajaNormal
        if filaCajaEmbAnc.isEmpty():
            return filaCajaEmbAnc
        return filaCajaDiscap
    # Tambien aplica para las embarazadas y los ancianos
    else:
        if filaCajaEmbAnc.isEmpty():
            return filaCajaEmbAnc
        if filaCajaNormal.isEmpty():
            return filaCajaNormal
        if filaCajaEmbAnc.isEmpty():
            return filaCajaDiscap
        return filaCajaEmbAnc


# Funcion para atender en caja y permitir que entren nuevos clientes (depende su condicion) cuando se liberan carritos
def atenderEnCaja(filaACobrar):
    global carritosDisponibles
    cliente = filaACobrar.sacarDeCola()  # Saca al cliente de la fila de caja
    carritoCliente = None

    for i in range(len(seguimientoCarritos)):
        if cliente == seguimientoCarritos[i].propietario:
            carritoCliente = seguimientoCarritos[i]
            break

    carritoCliente.propietario = None  # Libera al cliente del carrito
    carritoCliente.cola = None
    pilaCarritosDisponibles.agregarAPila(carritoCliente)  # Devuelve el carrito a la pila de carritos disponibles
    if filaCarritos.isEmpty():
        None
    else:
        # Una vez se libera un carrito, este pasa a ser propiedad de prioridad superior dentro de la cola de los carritos
        # El primer bucle itera tal que solo las embarazadas puedan pasar primero
        for i in range(filaCarritos.count):
            cliente = filaCarritos.sacarDeCola()
            if cliente.condicion == 3:
                carritoAsignado = pilaCarritosDisponibles.sacardePila()
                carritoAsignado.propietario = cliente
                prioridadColaCaja(cliente).agregarACola(cliente)
                return
            else:
                filaCarritos.agregarACola(cliente)
        # El segundo bucle itera tal que solo los ancianos puedan pasar segundos
        for i in range(filaCarritos.count):
            cliente = filaCarritos.sacarDeCola()
            if cliente.condicion == 4:
                carritoAsignado = pilaCarritosDisponibles.sacardePila()
                carritoAsignado.propietario = cliente
                prioridadColaCaja(cliente).agregarACola(cliente)
                return
            else:
                filaCarritos.agregarACola(cliente)
        # El tercer bucle itera tal que solo los discapacitados puedan pasar terceros
        for i in range(filaCarritos.count):
            cliente = filaCarritos.sacarDeCola()
            if cliente.condicion == 2:
                carritoAsignado = pilaCarritosDisponibles.sacardePila()
                carritoAsignado.propietario = cliente
                prioridadColaCaja(cliente).agregarACola(cliente)
                return
            else:
                filaCarritos.agregarACola(cliente)

        # Entran los normales
        cliente = filaCarritos.sacarDeCola()
        carritoAsignado = pilaCarritosDisponibles.sacardePila()
        carritoAsignado.propietario = cliente
        prioridadColaCaja(cliente).agregarACola(cliente)
        return


# Funcion para verificar si hay gente en la cola esperando en cada una de las cajas
def cobrarEnCaja():
    cajaNormalNoVacia = not filaCajaNormal.isEmpty()
    cajaDiscapNoVacia = not filaCajaDiscap.isEmpty()
    cajaEmbAncNoVacia = not filaCajaEmbAnc.isEmpty()

    if cajaNormalNoVacia:
        atenderEnCaja(filaCajaNormal)
    if cajaDiscapNoVacia:
        atenderEnCaja(filaCajaDiscap)
    if cajaEmbAncNoVacia:
        atenderEnCaja(filaCajaEmbAnc)


# Funcion para el ingreso de un cliente a la tienda
def ingresoDeCliente():
    global carritosDisponibles
    while True:
        condicionCliente = int(
            input("Ingrese la condición del cliente\n1) Normal\n2) Discapacitado\n3) Embarazada\n4) Anciano\nOpcion: "))
        try:
            cliente = Persona(condicionCliente)  # Crea un nuevo cliente con la condicion ingresada
            break
        except ValueError:
            print("Ingrese una condición válida\n")
    if pilaCarritosDisponibles.count >= 1:
        carritoAsignado = pilaCarritosDisponibles.sacardePila()
        carritoAsignado.propietario = cliente
        carritoAsignado.cola = prioridadColaCaja(cliente)
        prioridadColaCaja(cliente).agregarACola(cliente)
    else:
        filaCarritos.agregarACola(cliente)  # Agrega al cliente a la fila de carritos



# Función para generar los carritos disponibles inicialmente
def generarCarritos():
    for i in range(6):
        nuevoCarrito = Carrito()
        pilaCarritosDisponibles.agregarAPila(nuevoCarrito)
        seguimientoCarritos.append(nuevoCarrito)


# Creación de instancias de las estructuras de datos
filaCajaNormal = Queue()
filaCajaDiscap = Queue()
filaCajaEmbAnc = Queue()
filaCarritos = Queue()
pilaCarritosDisponibles = Pila()


# Función que muestra el menú de opciones
def menu():
    print("""
    Opciones
    ---------------
    [1]- Ingresa Cliente
    [2]- Cobrar Caja
    [3]- Mostrar Estado de carritos

    ---------------
    """)


# Función para limpiar la consola según el sistema operativo
def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    elif os.name == 'nt':
        _ = os.system('cls')


# Generación de los carritos disponibles inicialmente
generarCarritos()

# Bucle principal del programa
while True:
    menu()  # Mostrar menú de opciones
    ans = int(input("Opcion: "))  # Leer la opción seleccionada por el usuario
    clear()  # Limpiar la consola
    if ans == 1:
        ingresoDeCliente()  # Si la opción es 1, ingresar un cliente
        clear()  # Limpiar la consola
        displayEstadoGeneral()  # Mostrar el estado general de la tienda
        print("\n")  # Imprimir línea en blanco
    elif ans == 2:
        cobrarEnCaja()  # Si la opción es 2, cobrar en la caja
        displayEstadoGeneral()  # Mostrar el estado general de la tienda
        print("\n")  # Imprimir línea en blanco
    elif ans == 3:
        displayCarritos()  # Si la opción es 3, mostrar el estado de los carritos
        print("")  # Imprimir línea en blanco
    else:
        clear()  # Limpiar la consola
        print("Opción no válida")  # Imprimir mensaje de opción no válida
    
    
