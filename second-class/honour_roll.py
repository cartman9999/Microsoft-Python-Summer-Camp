gpa = float(input('Ingresa tu promedio: '))
lowest_grade = float(input('Ingres tu calificación máas baja: '))

honour_roll = False

if gpa >= 85 and lowest_grade >= 70:
    honour_roll = True

if honour_roll:
    print('Well done');
else: 
    print('Not honour roll');