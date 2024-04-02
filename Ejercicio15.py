'''Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos'''


minutes = int(input('Inserte minutos: '))

horas = minutes // 60
minutos = minutes % 60


print('Horas: {}'' ' 'Minutos: {}'.format(horas, minutos))

