'''Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.'''

spaghuetti_carbonara = 11
agua = 2
tiramisú = 5

lista_compra = [ spaghuetti_carbonara, agua, tiramisú ]

total = 0
for producto in lista_compra:
    total += producto

print('Total: ', (total) )
print ('Total + Propina 15%: ', (total *1.15))



  
