
opt=int(input('Tipo de conversion: 1 - milla a km 2- pulgada a cm: '))

if opt == 1 :
    long1=float(input('Ingrese milla a convertir: '))
    conv1=long1*1.60945
    print('Equivalente en km es: ',conv1)
elif opt == 2 :
    long2=float(input('Ingrese pulgada a convertir: '))
    conv2=long2*2.534
    print('Equivalente en cm es: ',conv2)

else:
    print('Seleccione opcion correcta')
