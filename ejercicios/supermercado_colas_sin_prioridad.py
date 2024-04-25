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
    if len(cliente_caja1.clientes) <= len(cliente_caja2.clientes) and 0 < carritos.contador<=6:
        cliente_caja1.agregar_cliente(nuevo_cliente)
        carritos.contador -= 1
        carritos.mostrar_estado()
        cliente_caja1.mostrar_estado()
        
    elif len(cliente_caja1.clientes) > len(cliente_caja2.clientes) and 0 < carritos.contador<=6:
        cliente_caja2.agregar_cliente(nuevo_cliente)
        carritos.contador -= 1
        carritos.mostrar_estado()
        cliente_caja2.mostrar_estado()
    else:
        cliente_espera.agregar_cliente(nuevo_cliente)

def control_fila_carrito():
    if carritos.contador > 0:
        if cliente_espera.clientes:
            if len(cliente_caja1.clientes) <= len(cliente_caja2.clientes):
                cliente_caja1.agregar_cliente(cliente_espera.siguiente_cliente())
            else:
                cliente_caja2.agregar_cliente(cliente_espera.siguiente_cliente())
            carritos.contador -= 1
        carritos.mostrar_estado()
    else:
        print("No hay carritos disponibles")

cliente_espera = ColaEspera()
cliente_caja1 = ColaCaja(1)
cliente_caja2 = ColaCaja(2)
carritos = Carrito()

def menu():
    print("""
Opciones
---------------
[1]-Ingresa Cliente
[2]-Cobrar Caja 1
[3]-Cobrar Caja 2
[4]-Ver Estado de Cajas
[5]-
[6]-
---------------
""")




while True:
    menu()
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        nuevo_cliente = Cliente("🧍🏻")
        mover_clientes_a_cajas()
    if opcion == 2:
        cliente_caja1.siguiente_cliente()
        carritos.contador+=1
        control_fila_carrito()
    if opcion == 3:
        cliente_caja2.siguiente_cliente()
        carritos.contador+=1
        control_fila_carrito()
    elif opcion == 4:
        print("------------------------")
        cliente_espera.mostrar_estado()
        print("------------------------")
        carritos.mostrar_estado()
        print("------------------------")
        cliente_caja1.mostrar_estado()
        print("------------------------")
        cliente_caja2.mostrar_estado()
        print("------------------------")
        

