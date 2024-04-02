''''Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.'''

print('Inserte texto: ')
texto = input()
vocales = 'a,e,i,o,u,A,E,I,O,U'

for letra in texto:
    if letra in vocales:
      print (letra)
