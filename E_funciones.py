print("Manejo de funciones")
def hola_mundo():
    print("HOLA MUNDO ARRIBA EL AME")

def mensa(msg):
    print(msg)

def escribeNC(nombre, apellido):
    print(f"Tu nombre completo es:  {nombre} {apellido}")

def suma2num(n1,n2):
    s = n1+n2
    return f"La suma de {n1} + {n2} es de: ",s
# Llamando a la funcion
hola_mundo()
mensa("HOLA WASAP") #LLama a mensa con 1 parametro
mensa("El profe me cacho enviando mensaje") #LLama a mensa con 1 parametro
escribeNC("Luis Cesar", "Cervantes")

print(" ")
print("Funciones que regresan valores")
print(suma2num(10,7))
print(suma2num(45,683))