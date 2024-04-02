'''Ejercicio 9: Conversor de Divisas
Ejercicios Introducción a Python: Enunciados 2
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.'''


dolares = float(input('Inserte dolares: '))

def conversor(dolares):
  return dolares * 0.85

print('La conversión a euros es de: ', conversor(dolares), '€')
