

print('Ingrese primer angulo: ')
grad1=int(input('grados: \n'))
min1=int(input('min: \n'))
seg1=int(input('seg: \n'))

print('Ingrese segundo angulo: ')
grad2=int(input('grados: \n'))
min2=int(input('min: \n'))
seg2=int(input('seg: \n'))

seg=seg1+seg2
if seg >=60:
    min_extra=seg // 60 #division enterea para quedarme con el cociente.Que luego le sumo a minutos.
    segfinal= seg % 60 #resto de la division, cantidad de segundos que nos quedan.
else:
    min_extra=0

min=min1+min2+min_extra

if min >=60:
    grad_extra=min // 60 #division entera para quedarme con el cociente.Que luego le sumo a grados.
    minfinal= min % 60 #resto de la division, cantidad de minutos que nos quedan.
else:
    grad_extra=0

grad=grad1+grad2+grad_extra

print(f"La suma de nuevo anguno es {grad} {minfinal}' {segfinal}'' ")


