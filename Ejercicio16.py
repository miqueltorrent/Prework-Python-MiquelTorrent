'''Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.'''

lista = [6,4,5,7,12,16,54,98]

contador_par = 0
contador_impar = 0

for number in lista:
  if number % 2 ==0:
    print(number, 'es par')
    contador_par += 1
  else:
    print(number, 'es impar')
    contador_impar += 1
print('El total de numeros pares es: ', contador_par)
print('El total de numeros impares es: ', contador_impar)