import urllib.request

def conteo_palabras(url):
    file = urllib.request.urlopen(url)
    leer = file.read()
    return len(leer.split())

url = input("Introduzca la url que quiera: \n")
print(conteo_palabras(url))
