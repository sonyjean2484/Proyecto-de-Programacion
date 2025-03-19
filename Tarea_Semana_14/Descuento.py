
#Función que calcula el valor de descuento aplicado al valor total de una compra
#Recibe como parámetros : valor de la compra
#Parámetro por defecto : porcentaje de descuento
def calcular_descuento(valor_compra,descuento=0.10):
    valor_descuento= (valor_compra*descuento)
    total_compra= valor_compra - valor_descuento
    return(valor_compra,valor_descuento,total_compra)

#Programa principal donde el usuario ingresa el valor de los productos
print("--------COMPRA DE PRODUCTOS--------")

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

#Llamada a la función
total= calcular_descuento(valor_compra)

etiqueta=["Total","Descuento","Total a Pagar"]
print("_"*40)

#Impresión de resultados: total, descuento y total a pagar
for i in range(len(total)):
      print(f"{etiqueta[i]} : $ {total[i]:.2f} ")







