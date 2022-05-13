
c1=float(input('Ingrese longitud de cateto uno: '))
c2=float(input('Ingrese longitud de cateto dos: '))

c1a=float(c1*c1)
c2a=float(c2*c2)

sumcat=float(c1a+c2a)

hip=float(sumcat**(1/2))

print('La longuitud de la hipotenusa del triangulo es: ',hip)
