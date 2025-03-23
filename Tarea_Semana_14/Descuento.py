
#Función que calcula el valor de descuento aplicado al valor total de una compra
#Recibe como parámetros : valor de la compra
#Parámetro por defecto : porcentaje de descuento
def calcular_descuento(valor_compra,descuento=0.10):
    valor_descuento= (valor_compra*descuento)
    total_compra= valor_compra - valor_descuento
    return (valor_compra,valor_descuento,total_compra)

#Función para imprimir los resultados
def impresion_resultados(total,etiqueta):
    for i in range(len(total)):
        print(f"{etiqueta[i]} : $ {total[i]:.2f} ")

#Programa principal donde el usuario ingresa el valor de los productos
print("--------COMPRA DE PRODUCTOS--------")
etiqueta=["Total","Descuento","Total a Pagar"]

#lista que almacena el valor de los productos
valor_productos= []
while True:
      valor= float(input("Ingrese el valor del producto: "))
      valor_productos.append(valor)
      opcion=input("Desea ingresar otro valor S/N ? : ")
      if (opcion!='s')and(opcion!='S'):
            break
print("_"*40)

#Impresión de productos comprados
print("Productos registrados")
for i in range(len(valor_productos)):
        print(f"Producto {i+1}: $ {valor_productos[i]}")
valor_compra= sum(valor_productos)
print("_"*40)

#Primera Llamada a la función.
# recibe como parámetro: total de la compra
total= calcular_descuento(valor_compra)
impresion_resultados(total,etiqueta)

print("_"*40)
#Segunda llamada a la función.
#recibe como parámetros: total de la compra y descuento
total= calcular_descuento(valor_compra,0.12)
impresion_resultados(total,etiqueta)









