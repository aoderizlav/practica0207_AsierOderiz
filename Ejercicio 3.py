def tabla_multi(n, m):

    file = "tabla-" + str(n) + ".txt"
    try:
        with open(file, "r") as file:
            lineas = file.readlines()
            print(lineas[m - 1])
    except FileNotFoundError:
        print("No existe el archivo que busca")
    return

n = int(input("Introduzca un numero del 1-10\n"))
m = int(input("Introduzca un numero del 1-10\n"))

tabla_multi(n, m)

