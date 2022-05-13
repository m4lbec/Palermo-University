
num=int(input('Ingresar numero de dos cifras: '))

if num > 50:
    a=num%10
    b=int((num%100)/10)
    print(a,b) # Esta bien que esten separados?