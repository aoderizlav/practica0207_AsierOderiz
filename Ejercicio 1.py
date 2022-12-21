def tabla_multi(n):
    if n in range(1, 11):
        file = open("tabla-" + str(n) + ".txt", "w")
        for tabla in range(1, 11):
            respuesta = str(tabla) + "*" + str(n) + "*" + str((tabla * n)) + "\n"
            file.write(respuesta)
    return

tabla_multi(8)
