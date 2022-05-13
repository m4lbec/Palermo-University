
"""num=int(input('Ingrese numero de tres digitos: '))

show=int(str(num)[1])

print('El segundo digito es: ',show)"""

numero=int(input('Ingrese valor: '))
if numero >= 100 and numero < 1000: #Para pedir que sea de tres digitos
    resultado1=numero//10
    resultado=resultado1%10

    print('El segundo digito es:  ',resultado)
    print(resultado1)

'''
Para numero de tres digitos, sacar el primero

    resultado=numero//100
    resultado=resultado%100
'''