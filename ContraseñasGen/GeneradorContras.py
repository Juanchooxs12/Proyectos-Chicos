import string
import random

#variable caracteres incluye todas las letras y simbolos que podria llevar la nueva contraseña
contra = ""
caracteres = string.ascii_uppercase + string.ascii_lowercase + "!#$%&/*+-._,(){}" + "0123456789"

#Se crea una contraseña aleatoria usando random para seleccionar al azar los caracteres
#random.SystemRandom() para agregar lo que se genere a la variable contra
#.choice() para seleccionar donde se sacan los caracteres
for i in range(16):
    contra += random.SystemRandom().choice(caracteres)
print(contra)