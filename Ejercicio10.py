'''Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''

dia = int(input('Inserte numero: '))

if dia ==1:
    print ('lunes')
elif dia == 2: 
  print('martes')
elif dia ==3: 
  print('miércoles')
elif dia==4:
  print('jueves')
elif dia ==5:
  print('viernes')
elif dia == 6: 
  print ('sabado')
elif dia == 7:
  print ('domingo')
else:
  print ('Ese dia no existe')