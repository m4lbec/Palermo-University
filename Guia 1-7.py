
edad1=int(input('Ingrese edad I:\n '))
edad2=int(input('Ingrese edad II:\n'))

if edad1 >= 18 or edad2 >= 18:
    if edad1 <= 18 or edad2 <= 18:
        prom=(edad1+edad2)/2
        print('El promedio es: ',prom)

    else:
        print('Las edades son ', edad1,' y ',edad2)
