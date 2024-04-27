import random

class Persona():
    def __init__(self, emoji):
        self.emoji = emoji

    def poner_emoji(lista_clientes):    
        emoji = random.choice(lista_clientes)
        persona = Persona(emoji)   
        return persona

lista_clientes = [1, 2, 3, 4]

pepe =Persona()

persona = pepe.poner_emoji(lista_clientes)




if persona.emoji == 1:
    print("Entró una viejardas")
elif persona.emoji == 2:
    print("Entró un mogo")
elif persona.emoji == 3:
    print("Entró una preñada")
else:
    print("Entró un normal")
