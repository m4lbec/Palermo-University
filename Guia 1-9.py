ingr=float(input('Ingrese ganancia anual de la empresa:\n'))

if ingr <= 10000:
    print('No aplicamos retenciones')
elif ingr > 10000 and ingr <= 15000:
    a=ingr-10000
    ret=a*0.2
    ingr2=ingr-ret
    print('El ingreso luego de aplicarle una retencion de ,',ret,' es ,', ingr2)
elif ingr > 15000:
    b=ingr-15000
    ret=(b*0.5)+300
    ingr2=ingr-ret
    print('El ingreso luego de aplicarle una retencion de, ',ret,' es ',ingr2)

