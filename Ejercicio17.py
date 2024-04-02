'''Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros.'''


millas=float(input('Introduzca millas: '))

def conversor_km(millas):
  return millas * 1.60934

print('{} millas equivale a'.format(millas), conversor_km(millas),' kilómetros')