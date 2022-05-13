
kmi=int(input('Ingrese kilometros iniciales: '))
kma=int(input('Ingrese kilometros recorridos: '))

kmr=kma+kmi
if kmr <= 100:
    print('Paciencia,falta mucho')
elif kmr > 100 and kmr < 200:
    print('Parar a desayunar')
elif kmr >= 200:
    print('Cargar combustible')