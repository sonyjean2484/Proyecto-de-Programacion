
#Creación de un diccionario que contiene información personal ficticia
#el diccionario tiene claves como: nombre, edad, ciudad y profesión

def impresion(informacion_personal,num):
    if num == 1:
        print("------DICCIONARIO ORIGINAL------")
    else:
        print("------DICCIONARIO MODIFICADO------")
    for clave, valor in informacion_personal.items():
        print(f"{clave}: {valor}")
    print("_" * 30)

informacion_personal = {
                        "Nombre": "Juan Perez",
                        "Edad":25,
                        "Ciudad": "Guayaquil",
                       }
#Impresión del diccionario original
impresion(informacion_personal,1)

#Accediendo a la clave Ciudad dentro del diccionario para modificarlo
for clave, valor in informacion_personal.items():
    if clave == "Ciudad":
         print("Clave y valor modificado")
         print (f"{clave}: {valor}")
         informacion_personal["Ciudad"]= "Quito" #modifica el valor de la clave Ciudad

#Agrega un nuevo elemento al diccionario
informacion_personal["Profesión"]= "Arquitectura"

#Verifica si la clave Teléfono existe en el diccionario
print("Teléfono" in informacion_personal,"La clave Teléfono no existe\n")

#Agrega la clave teléfono al diccionario
informacion_personal["Teléfono"]= "2813740"

#Eliminación de la clave edad
for clave, valor in informacion_personal.items():
    if clave == "Edad":
        del(informacion_personal["Edad"])
        break

#Imprime el diccionario con las modificaciones
impresion(informacion_personal,2)

