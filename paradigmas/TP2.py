import random   
import os


seguimientoCarritos = []
carritosDisponibles = 6

diccionarioCondiciones = {
        1 : "NORMAL",
        2 : "DISCAPACITADO",
        3 : "EMBARAZADA",
        4 :  "ANCIANO",
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
        self.propietario = None
        self.cola = None
        self.id = 10
    
    

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
        self.base = None
        self.count = 0
    
    def agregarAPila(self, item):
        nodoitem = Nodo(item)
        if self.tope is None:
            self.tope = nodoitem
            self.base = nodoitem
            self.count += 1
        else:
            self.tope.next = nodoitem
            self.tope = nodoitem
            self.count += 1
    
    def sacardePila(self):
        localcount = 0
        actual = self.base
        while localcount < self.count - 3:
            actual = actual.next
            localcount += 1
        viejoTope = actual
        self.tope = actual
        self.count -= 1
        return viejoTope.data

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
    try:
        for i in range(filaCarritos.size()):
            pilaCarritosString += filaCarritos.retornarElemento(i).representacion
    except:
        None
    carritosDisponiblesString = "[CARRITOS]"
    for i in range(carritosDisponibles):
        carritosDisponiblesString += "\U0001f6d2 "
    print(carritosDisponiblesString + "\t" + pilaCarritosString)

    filaCajaNormalString = "\n[CAJA N]\t"
    filaCajaDiscapString = "\n[CAJA D]\t"
    filacajaEmbAncString = "\n[CAJA E/A]\t"

    for i in range(filaCajaNormal.size()):
        filaCajaNormalString += filaCajaNormal.retornarElemento(i).representacion
    for i in range(filaCajaDiscap.size()):
        filaCajaDiscapString += filaCajaDiscap.retornarElemento(i).representacion
    for i in range(filaCajaEmbAnc.size()):
        filacajaEmbAncString += filaCajaEmbAnc.retornarElemento(i).representacion

    print(filaCajaNormalString, end="->")
    print(filaCajaDiscapString, end="->")
    print(filacajaEmbAncString, end="->")

def displayCarritos():
    for i in range(len(seguimientoCarritos)):
        carritoActual = seguimientoCarritos[i]
        propietario = carritoActual.propietario
        id = 20
        print(f"Estado de carrito {id}\nPropietario = El {diccionarioCondiciones[propietario.condicion]} {propietario.nombre}")
        


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


# esta función realiza el proceso de cobranza
def atenderEnCaja(filaACobrar):
    global carritosDisponibles
    filaACobrar.sacarDeCola()
    carritosDisponibles += 1
    if filaCarritos.isEmpty():
        None
    else:
        # el primer for itera tal que solo las embarazadas puedan pasar primero
        for i in range(filaCarritos.count):
            cliente = filaCarritos.sacarDeCola()
            if cliente.condicion == 3:
                prioridadColaCaja(cliente).agregarACola(cliente)
                carritosDisponibles -= 1
                return
            else:
                filaCarritos.agregarACola(cliente)
        # el segundo for itera tal que solo los ancianos puedan pasar segundos
        for i in range(filaCarritos.count):
            cliente = filaCarritos.sacarDeCola()
            if cliente.condicion == 4:
                prioridadColaCaja(cliente).agregarACola(cliente)
                carritosDisponibles -= 1
                return
            else:
                filaCarritos.agregarACola(cliente)
        # el tercer for itera tal que solo los discapacitados puedan pasar terceros
        for i in range(filaCarritos.count):
            cliente = filaCarritos.sacarDeCola()
            if cliente.condicion == 2:
                cliente = filaCarritos.sacarDeCola()
                prioridadColaCaja(cliente).agregarACola(cliente)
                carritosDisponibles -= 1
                return
            else:
                filaCarritos.agregarACola(cliente)
        # entran los normales
        cliente = filaCarritos.sacarDeCola()
        prioridadColaCaja(cliente).agregarACola(cliente)
        carritosDisponibles -= 1
        return

# esta función activa la cobranza segun la fila
def cobrarEnCaja():
    cajaNormalNoVacia = not filaCajaNormal.isEmpty()
    cajaDisacpNoVacia = not filaCajaDiscap.isEmpty()
    cajaEmbAncNoVacia = not filaCajaEmbAnc.isEmpty()

    if cajaNormalNoVacia:
        atenderEnCaja(filaCajaNormal)
    if cajaDisacpNoVacia:
        atenderEnCaja(filaCajaDiscap)
    if cajaEmbAncNoVacia:
        atenderEnCaja(filaCajaEmbAnc)

# esta funcion se encarga del tipo de cliente que ingresa a la tienda
def ingresoDeCliente():
    global carritosDisponibles
    while True:
        condicionCliente = int(input("Ingrese la condición del cliente\n1) Normal\n2) Discapacitado\n3) Embarazada\n4) Anciano\nOpcion: "))
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
        prioridadColaCaja(cliente).agregarACola(cliente)
    else:
        None

def generarCarritos():
    for i in range(6):
        nuevoCarrito = Carrito
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
    [4]-

    ---------------
    """)

def clear():
    if os.name =='posix':
        _ = os.system('clear')
    elif os.name =='nt':
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
