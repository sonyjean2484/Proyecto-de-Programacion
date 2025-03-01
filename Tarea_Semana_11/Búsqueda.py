
#creación del arreglo bidimensional matriz de 3x3
matriz =[
    [-3,0,5],
    [11,4,-6],
    [21,-9,1]
 ]

#Función que recorre la matriz en búsqueda del valor
def busqueda(matriz,numero):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                return(i,j)#retorna la posición del valor encontrado
    return None #retorna None si no se encuentra el valor

print("BÚSQUEDA LINEAL EN ARREGLOS BIDIMENSIONALES")
print("-------------------------------------------")
# valor que buscamos
numero = int(input("Ingrese el número para la búsqueda: "))
resultado = busqueda(matriz,numero)#llamamos a la función de búsqueda
if resultado:
   print(f"Se encontró el número {numero} ")
   print(f"Posición: {resultado}")
else:
    print(f"No se encontró el valor '{numero}' en la matriz")



