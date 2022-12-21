def tabla_multi(n):
    if n in range(1, 11):
        file = "tabla-" + str(n) + ".txt"
        try:
            file = open(file, "r")
        except FileNotFoundError:
            print("No existe el achivo")
        else:
         print(file.read())
    return


n = int(input("Introduzca un numero del 1-10\n"))
tabla_multi(n)

