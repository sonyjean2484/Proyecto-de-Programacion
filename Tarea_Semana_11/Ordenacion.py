#Definimos la matriz
matriz = [
    [5,3,4],
    [-2,-6,-1],
    [8,0,1]
]

print("MÉTODO DE ORDENACIÓN BUBLESORT")
print("--------------------------------")

#Función para ordenar una fila de manera ascendente
def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n-1):
        for j in range(n - i- 1):
            if fila[j] > fila[j + 1]:
                fila[j],fila[j + 1] = fila[j + 1],fila[j]

#Función para mostrar la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

#Muestra la matriz original
print("Matriz original:")
imprimir_matriz(matriz)

#Ordena cada fila de la matriz utilizando la función bubbleSort
for fila in matriz:
    bubble_sort_fila(fila)

#Muestra la matriz ordenada
print("Matriz ordenada por filas: ")
imprimir_matriz(matriz)