# listas
# almacena cualquier tipo de dato
names = ['Vianka', 'Eric']
scores = []

scores.append(70)
scores.append(90)

print(names)
print(scores)

print(scores[1])

# Longitud de la lista
print('Longitud: ' + str(len(names)))

# Insertar en posicion especifica
names.insert(0, 'Bill')
print(names)

# Ordernar lista
names.sort()
print(names)