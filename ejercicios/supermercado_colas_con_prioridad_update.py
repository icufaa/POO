"""
1-las colas de caja son de la siguiente manera:
CAJA prioridad embarazadas y ancianos
CAJA discapacitados
CAJA normal

2- Cuando ingresa una persona se debe indicar si la condicion especial (Embarazada- Anciano - discapacitado - normal)

3- Los carritos se entregan e usan prioridad, primero embarazadas, segundo ancianos, tercero discapacitado y por ultimo normal

4 - de acuerdo a su condicion van a la cola correspondiente

5- Si las colas especiales estan vacias, una normal puede ir a cualquiera de ellas

6- La salida de pantalla es con emoticonos

"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cliente:
    def __init__(self, emoji):
        self.emoji = emoji

class Carrito:
    def __init__(self):
        self.contador = 6


    def mostrar_estado(self):
        if 0 < self.contador <= 6:
            print(f"Carritos disponibles: {self.contador}")
        else:
            print("No hay carritos disponibles")

class ColaEspera:
    def __init__(self):
        self.clientes = []
    
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def siguiente_cliente(self):
        if self.clientes:
            return self.clientes.pop(0)
        else:
            return None
    
    def mostrar_estado(self):
        if self.clientes:
            print("Estado de la cola de espera:")
            lista_clientes =[cliente.emoji for cliente in self.clientes]
            print(lista_clientes)
        else:
            print("La cola de espera está vacía.")

class ColaCaja:
    def __init__(self,caja = int):
        self.clientes = []
        self.caja = caja
    
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def siguiente_cliente(self):
        if self.clientes:
            return self.clientes.pop(0)
        else:
            return None
    
    def mostrar_estado(self):
        if self.clientes:
            print(f"Estado de la Caja {self.caja}:")
            lista_caja = [cliente.emoji for cliente in self.clientes]
            print(lista_caja)
        else:
            print(f"La Caja {self.caja} esta vacia")
        



def mover_clientes_a_cajas():
    if len(caja_normales.clientes) <= len(caja_discapacitados.clientes) and len(caja_normales.clientes) <= len(caja_ancianos_embarazadas.clientes) and 0 < carritos.contador <=6:
        caja_normales.agregar_cliente(nuevo_cliente)
        carritos.contador -=1
        carritos.mostrar_estado()
        caja_normales.mostrar_estado()

    elif len(caja_ancianos_embarazadas.clientes) < len(caja_normales.clientes)and len(caja_ancianos_embarazadas.clientes) <= len(caja_discapacitados.clientes) and 0 < carritos.contador<=6:
        caja_ancianos_embarazadas.agregar_cliente(nuevo_cliente)
        carritos.contador -= 1
        carritos.mostrar_estado()
        caja_ancianos_embarazadas.mostrar_estado()
        
    elif len(caja_discapacitados.clientes) < len(caja_ancianos_embarazadas.clientes) and 0 < carritos.contador<=6:
        caja_discapacitados.agregar_cliente(nuevo_cliente)
        carritos.contador -= 1
        carritos.mostrar_estado()
        caja_discapacitados.mostrar_estado()

    else:
        cliente_espera.agregar_cliente(nuevo_cliente)

    if carritos.contador==0:
        print("No hay carritos disponibles")

def control_fila_carrito():
    if carritos.contador > 0:
        if cliente_espera.clientes:
            if len(caja_normales.clientes) < len(caja_ancianos_embarazadas.clientes) and len(caja_normales.clientes) < len(caja_discapacitados.clientes):
                caja_normales.agregar_cliente(cliente_espera.siguiente_cliente())

            # Si la caja de ancianos y embarzadas es menor o igual que todas las anteriores entra en Caja Ancianos
            elif len(caja_ancianos_embarazadas.clientes) < len(caja_discapacitados.clientes) and len(caja_ancianos_embarazadas.clientes)<len(caja_normales.clientes):
                caja_ancianos_embarazadas.agregar_cliente(cliente_espera.siguiente_cliente())

            # Si la caja discapacitados es menor que todas las anteriores entra en Caja discapacitados
            elif len(caja_discapacitados.clientes) < len(caja_ancianos_embarazadas.clientes) and len(caja_discapacitados.clientes) <len(caja_normales.clientes):
                caja_discapacitados.agregar_cliente(cliente_espera.siguiente_cliente())
            
            carritos.contador -= 1
        carritos.mostrar_estado()
    else:
        print("No hay carritos disponibles")

cliente_espera = ColaEspera()
caja_ancianos_embarazadas = ColaCaja("Anciandos y Embarazadas")
caja_discapacitados = ColaCaja("Discapactidados")
caja_normales = ColaCaja("Normales")
carritos = Carrito()

def menu():
    print("""
Opciones
---------------
[1]-Ingresa Cliente
[2]-Cobrar Caja Embarazadas-Viejas
[3]-Cobrar Caja Discapacitados
[4]-Cobrar Caja Normales
[5]-Ver Estado de Cajas
[6]-
[7]-
---------------
""")




while True:
    menu()
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        nuevo_cliente = Cliente("🧍🏻")
        mover_clientes_a_cajas()
    if opcion == 2:
        caja_ancianos_embarazadas.siguiente_cliente()
        carritos.contador+=1
        control_fila_carrito()
    if opcion == 3:
        caja_discapacitados.siguiente_cliente()
        carritos.contador+=1
        control_fila_carrito()
    if opcion ==4:
        caja_normales.siguiente_cliente()
        carritos.contador+=1
        control_fila_carrito()
    elif opcion == 5:
        print("------------------------")
        cliente_espera.mostrar_estado()
        print("------------------------")
        carritos.mostrar_estado()
        print("------------------------")
        caja_ancianos_embarazadas.mostrar_estado()
        print("------------------------")
        caja_discapacitados.mostrar_estado()
        print("------------------------")
        caja_normales.mostrar_estado()
        print("------------------------")
    else:
        input("Presione una tecla para continuar...")
        


