
num=int(input('Ingrese numero: \n'))
num2=int(input('Ingrese segundo numero: \n'))

if num>0 and num2>0:
    print('El producto sera positivo')
elif num==0 or num2 ==0:
    print('El producto sera nulo')
elif num<0 or num2<0:
    print('El producto sera un numero negativo')
