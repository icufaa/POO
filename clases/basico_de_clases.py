class Celular:
    def __init__(self,modelo=None,marca=None,camara=None):
        self.modelo = modelo
        self.marca = marca
        self.camara = camara



    def cargar_modelo(self):
        self.modelo = input("Que modelo quiere ingresar?: ")
        self.marca = input("Que marca quiere ingresar?: ")
        self.camara = int(input("Megapixeles: "))

#Creo una instancia de la clase Celular

mi_celular = Celular()

#Llamo al metodo cargar_modelo en la instancia

mi_celular.cargar_modelo()


#Printeo la marca
print(f"marca: {mi_celular.marca}")



