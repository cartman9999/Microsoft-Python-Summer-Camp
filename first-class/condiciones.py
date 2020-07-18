precio = input("Ingresa un número: ")

impuesto = 0

if float(precio) >= 1.00:
    impuesto = 0.07

print('Impuesto: ' + str(impuesto))