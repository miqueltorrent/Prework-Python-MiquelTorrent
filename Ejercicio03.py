'''Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no.'''

print ('Inserte edad: ')
edad = int(input())

if edad >= 18:
  print('El usuario es mayor de edad')
else:
  print('El usuario es menor de edad')
