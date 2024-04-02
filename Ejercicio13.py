'''Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no'''

numero = int(input('Ingrese número: '))
contador = 0

if numero > 1:
  for x in range(2,numero):
    resultado=numero%x
    if resultado ==0: 
      contador += 1
if contador == 0:
  print ('El numero es primo')
else: 
  print('El numero no es primo')



