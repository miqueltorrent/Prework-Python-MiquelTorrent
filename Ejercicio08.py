'''Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.'''

print ('Inserte su peso: ')
peso = float(input())
print ('Inserte su altura: ')
altura = float(input())

def imc(peso, altura):

  return (peso / altura ** 2)

print('Su IMC es: ', imc(peso, altura))
