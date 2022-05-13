
num=int(input('Ingrese un numero:\n'))
if num > 0:
    raiz=num**(1/2)
    print('La raiz es ',raiz)
elif num < 0:
    cuadrado=num*num
    print('El cuadrado es ',cuadrado)
elif num == 0:
    print('Error. Ha ingresado valor nulo')


