import random

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cliente:
    def __init__(self, emoji):
        self.emoji = emoji
    
    @staticmethod
    def poner_emoji(emoji):
        return Cliente(emoji)


class Carrito:
    def __init__(self):
        self.contador = 6

    def mostrar_estado(self):
        if 0 < self.contador <= 6:
            print(f"Carritos disponibles: {self.contador}")

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
    def __init__(self, caja=int):
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

flag_cliente = None

def control_cliente_que_entra(nuevo_cliente):
    global flag_cliente
    if nuevo_cliente.emoji not in['👵',"♿","🤰🏻"]:
        flag_cliente = nuevo_cliente.emoji
    elif nuevo_cliente.emoji not in ["🧍","🤰🏻",'👵']:
        flag_cliente = nuevo_cliente.emoji
    elif nuevo_cliente.emoji not in ["🧍","🤰🏻",'♿']:
        flag_cliente = nuevo_cliente.emoji
    elif nuevo_cliente.emoji not in ['👵',"♿","🧍"]:
        flag_cliente = nuevo_cliente.emoji
    


def mover_clientes_a_cajas():
    global flag_cliente
    nuevo_cliente = Cliente.poner_emoji(random.choice(["👵", "♿", "🤰🏻", "🧍"]))
    control_cliente_que_entra(nuevo_cliente)


    def mover_final():
        if len(caja_normales.clientes) <= len(caja_discapacitados.clientes) and len(caja_normales.clientes) <= len(caja_ancianos_embarazadas.clientes) and 0 < carritos.contador <= 6 or len(caja_normales.clientes) == 0 or len(caja_ancianos_embarazadas.clientes) == 0 or len(caja_discapacitados.clientes) == 0:
            caja_normales.agregar_cliente(nuevo_cliente)
            carritos.contador -=1
            carritos.mostrar_estado()
            caja_normales.mostrar_estado()
            

        elif len(caja_ancianos_embarazadas.clientes) < len(caja_normales.clientes)and len(caja_ancianos_embarazadas.clientes) <= len(caja_discapacitados.clientes) and 0 < carritos.contador<=6 or len(caja_normales.clientes) == 0 or len(caja_ancianos_embarazadas.clientes) == 0 or len(caja_discapacitados.clientes) == 0:
            caja_ancianos_embarazadas.agregar_cliente(nuevo_cliente)
            carritos.contador -= 1
            carritos.mostrar_estado()
            caja_ancianos_embarazadas.mostrar_estado()
            
        elif len(caja_discapacitados.clientes) < len(caja_ancianos_embarazadas.clientes) and 0 < carritos.contador<=6 or len(caja_normales.clientes) == 0 or len(caja_ancianos_embarazadas.clientes) == 0 or len(caja_discapacitados.clientes) == 0:
            caja_discapacitados.agregar_cliente(nuevo_cliente)
            carritos.contador -= 1
            carritos.mostrar_estado()
            caja_discapacitados.mostrar_estado()

        else:
            cliente_espera.agregar_cliente(nuevo_cliente)

    
    if flag_cliente =="🧍" and flag_cliente:
        mover_final()
    elif flag_cliente == "🤰🏻":
        if carritos.contador> 0:
            caja_ancianos_embarazadas.agregar_cliente(nuevo_cliente)
            carritos.contador -=1
            carritos.mostrar_estado()
            caja_ancianos_embarazadas.mostrar_estado()
        else:
            mover_final()
    elif flag_cliente == "♿":
        if carritos.contador>0:
            caja_discapacitados.agregar_cliente(nuevo_cliente)
            carritos.contador -=1
            carritos.mostrar_estado()
            caja_discapacitados.mostrar_estado()
        else:
            mover_final()
    elif flag_cliente == "👵":
        if carritos.contador>0:
            caja_ancianos_embarazadas.agregar_cliente(nuevo_cliente)
            carritos.contador -=1
            carritos.mostrar_estado()
            caja_ancianos_embarazadas.mostrar_estado()
        else:
            mover_final()



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
    elif carritos.contador == 0:
        print("No hay carritos disponibles, pasa a cola de espera")




cliente_espera = ColaEspera()
caja_ancianos_embarazadas = ColaCaja("Anciandos y Embarazadas")
caja_discapacitados = ColaCaja("Discapactidados")
caja_normales = ColaCaja("Normales")
carritos = Carrito()

def menu():
    print("""
Opciones
-----------------------------------
[1]-Ingresa Cliente
[2]-Cobrar Caja Embarazadas-Viejas
[3]-Cobrar Caja Discapacitados
[4]-Cobrar Caja Normales
[5]-Ver Estado de Cajas
-----------------------------------
""")


while True:
    menu()
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        if carritos.contador == 0:
            print("No hay carritos disponible, pasa a cola de espera")
        mover_clientes_a_cajas()
        
    if opcion == 2:
        caja_ancianos_embarazadas.siguiente_cliente()
        print("Se ha cobrado En Caja Ancianos/Embarazadas, Pasa el siguiente")
        carritos.contador+=1
        control_fila_carrito()
    if opcion == 3:
        caja_discapacitados.siguiente_cliente()
        print("Se ha cobrado En Caja Discapacitados, Pasa el siguiente")
        carritos.contador+=1
        control_fila_carrito()
    if opcion ==4:
        caja_normales.siguiente_cliente()
        print("Se ha cobrado En Caja Normales, Pasa el siguiente")
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
