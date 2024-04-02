'''Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo.'''

longitud = float(input('Inserte longitud(cm): '))
ancho = float(input('Inserte ancho(cm): '))

def area_rectangulo (longitud, ancho):
  return longitud * ancho

print ((area_rectangulo(longitud, ancho)),'cm²')


