class Objeto:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.nombre}: {self.descripcion}"

    def obtener_nombre(self):
        return self.nombre

    def obtener_descripcion(self):
        return self.descripcion

    def establecer_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def establecer_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un objeto
    objeto1 = Objeto("Ejemplo", "Esto es un objeto de ejemplo")

    # Imprimir el objeto
    print(objeto1)

    # Obtener nombre y descripción
    print("Nombre:", objeto1.obtener_nombre())
    print("Descripción:", objeto1.obtener_descripcion())

    # Establecer nuevo nombre y descripción
    objeto1.establecer_nombre("Nuevo Ejemplo")
    objeto1.establecer_descripcion("Esto es un nuevo objeto de ejemplo")

    # Imprimir el objeto actualizado
    print(objeto1)
