
cod=int(input('Ingrese codigo de llamada:\n1-Local\n2-Interurbana\n3-Internacional\n'))
min=int(input('Cuantos minutos desea llamar? '))

if cod == 1:
    llam=(min*0.25)
    print('La llamada tendra un costo de ',llam)
elif cod == 2:
    llam=(min*0.40)
    print('La llamada tendra un costo de ',llam)
elif cod == 3:
    llam=(min*1.05)
    print('La llamada tendra un costo de ',llam)