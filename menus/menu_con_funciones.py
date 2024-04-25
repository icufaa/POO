def funcion1():
    print("Has seleccionado la opción 1.")

def funcion2():
    print("Has seleccionado la opción 2.")

def funcion3():
    print("Has seleccionado la opción 3.")

def salir():
    print("Saliendo del programa.")
    exit()

def menu():
    while True:
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Opción 3")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            funcion1()
        elif opcion == "2":
            funcion2()
        elif opcion == "3":
            funcion3()
        elif opcion == "4":
            salir()
        else:
            print("Opción inválida. Inténtalo de nuevo.")


menu()
