
ang=int(input('Ingrese valor de angulo -> \n'))

if ang > 180:
    print('Angulo no valido')
    ang =int(input('Ingrese un nuevo angulo: \n')) 
if ang <= 90:
    print('Es un angulo agudo')
elif ang == 90:
    print('Es un angulo recto')
elif ang > 90 and ang < 180:
    print('Es un angulo obtuso')
elif ang == 180:
    print('Angulo llano')
 