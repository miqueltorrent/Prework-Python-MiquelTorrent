'''Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.'''

lista = str(input('Inserte texto: '))

def contador_palabras(lista):
  palabras = lista.split()
  cantidad_palabras = len(palabras)
  return cantidad_palabras

print(f'La cantidad de palabras es: ', contador_palabras(lista))

