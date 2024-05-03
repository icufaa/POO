# TRABAJO PRACTICO N2 -
# MEYER IVÁN - VIÑALES FACUNDO

import random
import os


seguimientoCarritos = []
carritosDisponibles = 0


diccionarioCondiciones = {
    1: "NORMAL",
    2: "DISCAPACITADO",
    3: "EMBARAZADA",
    4: "ANCIANO",
}

lista_clientes = [
    "Juan", "María", "Pedro", "Ana", "Luis", "Sofía", "Carlos", "Laura", "Miguel", "Isabel",
    "Alejandro", "Lucía", "Javier", "Elena", "Diego", "Carmen", "Jorge", "Teresa", "Roberto", "Paula",
    "José", "Silvia", "Fernando", "Raquel", "Andrés", "Natalia", "Antonio", "Patricia", "Rafael", "Eva",
    "Francisco", "Marina", "Pablo", "Beatriz", "David", "Adriana", "Daniel", "Clara", "Joaquín", "Nuria",
    "Manuel", "Sara", "Ángel", "Cristina", "Ricardo", "Verónica", "Alberto", "Inés", "Guillermo", "Victoria"
]


class Carrito():
    def __init__(self) -> None:
        global carritosDisponibles
        carritosDisponibles += 1
        self.propietario = None
        self.cola = None
        self.id = carritosDisponibles


class Persona():
    def __init__(self, condicion):
        self.condicion = condicion
        self.representacion = diccionarioCondiciones[condicion][0]
        self.nombre = random.choice(lista_clientes)

    @property
    def condicion(self):
        return self._condicion

    @condicion.setter
    def condicion(self, value):
        if value in list(diccionarioCondiciones.keys()):
            self._condicion = value
        else:
            raise ValueError("Condicion ingresada no válida")


class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


class Pila:
    def __init__(self):
        self.tope = None
        self.count = 0

    def agregarAPila(self, item):
        nodoitem = Nodo(item)
        if self.tope is None:
            self.tope = nodoitem
            self.count += 1
        else:
            nodoitem.next = self.tope
            self.tope = nodoitem
            self.count += 1

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

    def estaEnPila(self, value):
        localcount = 0
        actual = self.tope
        while localcount < self.count:
            if actual.data == value:
                return True
            actual = actual.next
            localcount += 1
        return False


class Queue:
    def __init__(self):
        self.final = None
        self.frente = None
        self.count = 0

    def sacarDeCola(self):
        if self.frente is None:
            print('Cola vacia')
        actual = self.frente
        self.frente = self.frente.next
        if self.frente is None:
            self.final = None
        self.count -= 1
        return actual.data

    def agregarACola(self, item):
        nodo = Nodo(item)

        if self.frente is None:
            self.frente = nodo
            self.final = nodo
        else:
            self.final.next = nodo
            self.final = nodo
        self.count += 1

    # funcion que puede tanto retornar un elemento como eliminarlo mediante un indice
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

    def isEmpty(self):
        return self.final is None and self.frente is None

    def size(self):
        return self.count


# funcion para mostrar gráficamente el estado de la tienda
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
    print(carritosDisponiblesString + "\t" + pilaCarritosString)

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

# esta funcion determina a donde va a ir la persona de acuerdo a su condicion
def prioridadColaCaja(clientearg):
    condicionVal = diccionarioCondiciones[clientearg.condicion]
    # si es normal, se fija si las demás filas estan vacias y se mete si es así
    if condicionVal == diccionarioCondiciones[1]:
        if filaCajaNormal.isEmpty():
            return filaCajaNormal
        if filaCajaDiscap.isEmpty():
            return filaCajaDiscap
        if filaCajaEmbAnc.isEmpty():
            return filaCajaEmbAnc
        return filaCajaNormal
    # mismo caso para los discapacitados
    elif condicionVal == diccionarioCondiciones[2]:
        if filaCajaDiscap.isEmpty():
            return filaCajaDiscap
        if filaCajaNormal.isEmpty():
            return filaCajaNormal
        if filaCajaEmbAnc.isEmpty():
            return filaCajaEmbAnc
        return filaCajaDiscap
    # tambien aplica para las embarazadas y los ancianos
    else:
        if filaCajaEmbAnc.isEmpty():
            return filaCajaEmbAnc
        if filaCajaNormal.isEmpty():
            return filaCajaNormal
        if filaCajaEmbAnc.isEmpty():
            return filaCajaDiscap
        return filaCajaEmbAnc


# esta función realiza la atencion en caja y a su vez permite que entren nuevos clientes (de acuerdo a su condicion)
# cuando se liberan carritos
def atenderEnCaja(filaACobrar):
    global carritosDisponibles
    cliente = filaACobrar.sacarDeCola()
    carritoCliente = None

    for i in range(len(seguimientoCarritos)):
        if cliente == seguimientoCarritos[i].propietario:
            carritoCliente = seguimientoCarritos[i]
            break

    carritoCliente.propietario = None
    carritoCliente.cola = None
    pilaCarritosDisponibles.agregarAPila(carritoCliente)
    if filaCarritos.isEmpty():
        None
    else:
        # una vez se libera un carrito, este pasa a ser propiedad de prioridad superior dentro de la cola de los carritos   z
        # el primer for itera tal que solo las embarazadas puedan pasar primero
        for i in range(filaCarritos.count):
            cliente = filaCarritos.sacarDeCola()
            if cliente.condicion == 3:
                carritoAsignado = pilaCarritosDisponibles.sacardePila()
                carritoAsignado.propietario = cliente
                prioridadColaCaja(cliente).agregarACola(cliente)
                return
            else:
                filaCarritos.agregarACola(cliente)
        # el segundo for itera tal que solo los ancianos puedan pasar segundos
        for i in range(filaCarritos.count):
            cliente = filaCarritos.sacarDeCola()
            if cliente.condicion == 4:
                carritoAsignado = pilaCarritosDisponibles.sacardePila()
                carritoAsignado.propietario = cliente
                prioridadColaCaja(cliente).agregarACola(cliente)
                return
            else:
                filaCarritos.agregarACola(cliente)
        # el tercer for itera tal que solo los discapacitados puedan pasar terceros
        for i in range(filaCarritos.count):
            cliente = filaCarritos.sacarDeCola()
            if cliente.condicion == 2:
                carritoAsignado = pilaCarritosDisponibles.sacardePila()
                carritoAsignado.propietario = cliente
                prioridadColaCaja(cliente).agregarACola(cliente)
                return
            else:
                filaCarritos.agregarACola(cliente)

        # entran los normales
        cliente = filaCarritos.sacarDeCola()
        carritoAsignado = pilaCarritosDisponibles.sacardePila()
        carritoAsignado.propietario = cliente
        prioridadColaCaja(cliente).agregarACola(cliente)
        return


# esta función se fija si hay gente en la cola esperando en cada una de las cajas, si se da el caso de que en una no hay gente,
# no se realiza ningun proceso de cobranza
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



# esta funcion se encarga del tipo de cliente que ingresa a la tienda
def ingresoDeCliente():
    global carritosDisponibles
    while True:
        condicionCliente = int(
            input("Ingrese la condición del cliente\n1) Normal\n2) Discapacitado\n3) Embarazada\n4) Anciano\nOpcion: "))
        try:
            cliente = Persona(condicionCliente)
            break
        except ValueError:
            print("Ingrese una condición válida\n")
    filaCarritos.agregarACola(cliente)
    if pilaCarritosDisponibles.count >= 1:
        cliente = filaCarritos.sacarDeCola()
        carritoAsignado = pilaCarritosDisponibles.sacardePila()
        carritoAsignado.propietario = cliente
        carritoAsignado.cola = prioridadColaCaja(cliente)
        prioridadColaCaja(cliente).agregarACola(cliente)


def generarCarritos():
    for i in range(6):
        nuevoCarrito = Carrito()
        pilaCarritosDisponibles.agregarAPila(nuevoCarrito)
        seguimientoCarritos.append(nuevoCarrito)



filaCajaNormal = Queue()
filaCajaDiscap = Queue()
filaCajaEmbAnc = Queue()
filaCarritos = Queue()
pilaCarritosDisponibles = Pila()


def menu():
    print("""
    Opciones
    ---------------
    [1]- Ingresa Cliente
    [2]- Cobrar Caja
    [3]- Mostrar Estado de carritos

    ---------------
    """)


def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    elif os.name == 'nt':
        _ = os.system('cls')


generarCarritos()

while True:
    menu()
    ans = int(input("Opcion: "))
    clear()
    if ans == 1:
        ingresoDeCliente()
        clear()
        displayEstadoGeneral()
        print("\n")
    elif ans == 2:
        cobrarEnCaja()
        displayEstadoGeneral()
        print("\n")
    elif ans == 3:
        displayCarritos()
        print("")
    else:
        clear()
        print("Opción no válida")
