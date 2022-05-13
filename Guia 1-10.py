tiem=int(input('Ingrese la cantidad de horas-SI CORRESPONDE-que ha estado estacionado:\n'))
tiem2=int(input('Ingrese la cantidad de min que ha estado estacionado:\n'))
if tiem == 0:
    if tiem2 > 0 and tiem2>15:
        imp=45+45
        print('Debe pagar: ',imp)
    elif tiem2 > 0 and tiem2 <= 15:
        imp=45
        print('Debe abonar: ',imp)
elif tiem > 0 and tiem2==0:
    imp=(45*tiem)+45
    print('Debe abonar: ',imp)
elif tiem > 0 and tiem2 <= 15:
    imp=(45*tiem)+45
    print('Debe abonar: ')
elif tiem > 0 and tiem2 > 15:
    imp=(45*tiem)+90
    print('Debe abonar: ',imp)

'''
a=int(input("Ingrese lado A:\n"))
b=int(input("Ingrese lado B:\n"))
print("la longitud de la hipotenusa es: %.2f" %(a**2+b**2))**0.5 #%.2f solo para dos decimales.
'''
'''
hora=int(input("Ingrese cantidad de horas:\n"))
if (hora==0):
   print("El importe a abonar es: " , 45)
else: 
    minutos=int(input("Ingrese cantidad de minutos:\n"))
    if(minutos>15):
        print("El importe a abonar es: %.2f" %((hora+1)*45))
    else:
        print("El importe a abonar es: %.2f" %((hora)*45))
'''