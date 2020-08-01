x = int(input())
y = int(input())

try:
    print(x/y)
except ZeroDivisionError as error:
    print('No se puede dividir entre cero')
else:
    print('Hubo un error distinto a dividir entre cero')
finally:
    print('Fin')
