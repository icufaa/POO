import random
import os


def clear():
    if os.name =='posix':
        _ = os.system('clear')
    elif os.name =='nt':
        _ = os.system('cls')

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
        if 0 <= self.contador <= 6:
            
            print(f"\nCarritos disponibles: {self.contador}")
        

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
    
    def mostrar_estado(self,prioridades):
        if self.clientes:
            print(f"Estado de la Caja {self.caja}:")
            lista_caja = ordenar_por_prioridad([cliente.emoji for cliente in self.clientes],prioridades)
            print(lista_caja)
        else:
            print(f"\nLa Caja {self.caja} esta vacia")

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
    print(f'{nuevo_cliente.emoji} entro a la tienda')
    print('--------------------------------')


    def mover_final():
        if len(caja_normales.clientes) <= len(caja_discapacitados.clientes) and len(caja_normales.clientes) <= len(caja_ancianos_embarazadas.clientes) and 0 < carritos.contador <= 6 or len(caja_normales.clientes) == 0 or len(caja_ancianos_embarazadas.clientes) == 0 or len(caja_discapacitados.clientes) == 0:
            caja_normales.agregar_cliente(nuevo_cliente)
            carritos.contador -=1


        elif len(caja_ancianos_embarazadas.clientes) < len(caja_normales.clientes)and len(caja_ancianos_embarazadas.clientes) <= len(caja_discapacitados.clientes) and 0 < carritos.contador<=6 or len(caja_normales.clientes) == 0 or len(caja_ancianos_embarazadas.clientes) == 0 or len(caja_discapacitados.clientes) == 0:
            caja_ancianos_embarazadas.agregar_cliente(nuevo_cliente)
            carritos.contador -= 1
            
            
        elif len(caja_discapacitados.clientes) < len(caja_ancianos_embarazadas.clientes) and 0 < carritos.contador<=6 or len(caja_normales.clientes) == 0 or len(caja_ancianos_embarazadas.clientes) == 0 or len(caja_discapacitados.clientes) == 0:
            caja_discapacitados.agregar_cliente(nuevo_cliente)
            carritos.contador -= 1

        else:
            cliente_espera.agregar_cliente(nuevo_cliente)

    
    if flag_cliente =="🧍" and carritos.contador>0:
        mover_final()
    elif flag_cliente == "🤰🏻":
        caja_ancianos_embarazadas.agregar_cliente(nuevo_cliente)
        carritos.contador -=1

    elif flag_cliente == "♿":
        caja_discapacitados.agregar_cliente(nuevo_cliente)
        carritos.contador -=1
        
    elif flag_cliente == "👵":

        caja_ancianos_embarazadas.agregar_cliente(nuevo_cliente)
        carritos.contador -=1
        
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

            else:
                caja_normales.agregar_cliente(cliente_espera.siguiente_cliente())
            
            carritos.contador -= 1
    elif carritos.contador == 0:
        print("\nNo hay carritos disponibles, pasa a cola de espera\n")


def mostrar_estados_de_las_filas(prioridad_embarazadas,prioridad_discapacitados):
    print("------------------------")
    cliente_espera.mostrar_estado()
    print("------------------------")
    carritos.mostrar_estado()
    print("------------------------")
    caja_ancianos_embarazadas.mostrar_estado(prioridad_embarazadas)
    print("------------------------")
    caja_discapacitados.mostrar_estado(prioridad_discapacitados)
    print("------------------------")
    caja_normales.mostrar_estado({})
    print("------------------------")



def ordenar_por_prioridad(lista,prioridades):
    return sorted(lista,key=lambda x:prioridades.get(x,float('inf')))

#Diccionario de prioridades
prioridad_discapacitados = {
    "♿": 1,
    "👵": 2,      
    "🤰🏻": 2,  
    "🧍": 4 
}
prioridad_embarazadas ={
    "🤰🏻": 1,
    "♿": 2,      
    "👵": 1,  
    "🧍": 4 

}


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
-----------------------------------
""")


while True:
    menu()
    opcion = int(input("Ingrese una opcion: "))
    print(" ")
    clear()
    if opcion == 1:
        if carritos.contador == 0:
            print("\nNo hay carritos disponible, pasa a cola de espera\n")
            nuevo_cliente = Cliente.poner_emoji(random.choice(["👵", "♿", "🤰🏻", "🧍"]))
            cliente_espera.agregar_cliente(nuevo_cliente)
            mostrar_estados_de_las_filas(prioridad_embarazadas,prioridad_discapacitados)
        else:
            mover_clientes_a_cajas() 
            mostrar_estados_de_las_filas(prioridad_embarazadas,prioridad_discapacitados) 
    if opcion == 2:
        caja_ancianos_embarazadas.siguiente_cliente()
        print("\nSe ha cobrado En Caja Ancianos/Embarazadas, Pasa el siguiente\n")
        carritos.contador+=1
        control_fila_carrito()
        print('Avanza la fila')
        mostrar_estados_de_las_filas(prioridad_embarazadas,prioridad_discapacitados)
    if opcion == 3:

        caja_discapacitados.siguiente_cliente()
        print("\nSe ha cobrado En Caja Discapacitados, Pasa el siguiente\n")
        carritos.contador+=1
        control_fila_carrito()
        print('Avanza la fila')
        mostrar_estados_de_las_filas(prioridad_embarazadas,prioridad_discapacitados)
    if opcion ==4:
        caja_normales.siguiente_cliente()
        print("\nSe ha cobrado En Caja Normales, Pasa el siguiente\n")
        carritos.contador+=1
        control_fila_carrito()
        print('Avanza la fila')
        mostrar_estados_de_las_filas(prioridad_embarazadas,prioridad_discapacitados)
    else:
        
        input("\nPresione una tecla para continuar... ")
        clear()
