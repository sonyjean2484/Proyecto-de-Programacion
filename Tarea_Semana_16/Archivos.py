#Creación y manejo de archivos en Phyton

#Definición del nombre del archivo
my_file = "my_notes.txt"

#Abrimos el archivo que creamos
#Modo de apertura del archivo: "w" para escritura (write)
archivo_escritura = open(my_file, "w")

#Metodo write() : para escribir una línea a la vez
archivo_escritura.write("Mi nombre es Sonia Vásquez\n")
archivo_escritura.write("Vivo en la ciudad de Quito\n")
archivo_escritura.write("Soy casada y tengo 3 hijos\n")
archivo_escritura.write("Estudio Tecnologías de la Información en la UEA\n")
archivo_escritura.write("Esto es una tarea de Programacion\n")
archivo_escritura.write("Creación y manejo de archivos en Python\n")

#Cerramos el archivo de escritura
archivo_escritura.close()

#Apertura del archivo: modo "r" para lectura (read)
archivo_lectura = open(my_file, "r")

#Metodo readline() : lee una línea a la vez
archivo_lectura.seek(0)# Reinicio del cursor al inicio del archivo
linea1 = archivo_lectura.readline()
linea2 = archivo_lectura.readline()
linea3 = archivo_lectura.readline()
linea4 = archivo_lectura.readline()
linea5 = archivo_lectura.readline()
linea6 = archivo_lectura.readline()

#Muestra en pantalla la lectura de cada línea del archivo
print("\nContenido de my_file línea por línea usando readline() : ")
print("Línea 1:", linea1.strip()) #elimina el salto de línea al final
print("Línea 2:", linea2.strip())
print("Línea 3:", linea3.strip())
print("Línea 4:", linea4.strip())
print("Línea 5:", linea5.strip())
print("Línea 6:", linea6.strip())

#Cierre del archivo de lectura
archivo_lectura.close()
