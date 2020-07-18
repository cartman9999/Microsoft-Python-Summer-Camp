
country = input("¿De que pais eres? ").lower()

if country == 'canada':
    province = input("¿De que provincia eres? ").lower();
    
    if province in ('alberta', 'nunavut', 'yukon'):
        tax = 0.05
    elif province == 'ontario':
        tax = 0.13
    else:
        tax = 0.15    
else:
    tax = 0

print('El impuesto es de ' + str(tax));
