'''Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.'''

Precio = float(input('Introduzca precio del producto: '))

def calculadora_descuento(Precio):
  return Precio * 0.8
print ('El precio final es: ',calculadora_descuento(Precio),'€')