def opcion_1():
    print("Has seleccionado la opción 1.")
    # Aquí colocarías el código correspondiente a la opción 1

def opcion_2():
    print("Has seleccionado la opción 2.")
    # Aquí colocarías el código correspondiente a la opción 2

def opcion_3():
    print("Has seleccionado la opción 3.")
    # Aquí colocarías el código correspondiente a la opción 3

def salir():
    print("Saliendo del programa.")
    # Aquí podrías agregar código de limpieza o cualquier otra acción antes de salir
    exit()

def menu():
    while True:
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Opción 3")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            opcion_1()
        elif opcion == "2":
            opcion_2()
        elif opcion == "3":
            opcion_3()
        elif opcion == "4":
            salir()
        else:
            print("Opción inválida. Inténtalo de nuevo.")

# Para ejecutar el menú, simplemente llamas a la función menu():
menu()
