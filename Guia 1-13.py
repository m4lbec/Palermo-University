print('Piensa en cualquiera de los tres personajes siguientes:\n1-Mirta Legrand\n2-Lionel Messi\n3-Mauricio Macri\n')
print('Te hare unas preguntas para adivinar tu personaje\n')
 
sex=int(input('Tu personaje, es:\n1-Hombre\n2-Mujer\n'))
edad=int(input('Tu personaje, tiene mas de 40 años?:\n1-si\n2-no\n'))
prof=int(input('Tu personaje, es:\n1-Futbolista\n2-Politico\n3-Conductora de television\n'))

if sex == 1 and prof==1 and edad ==2:
    print('Es Messi')
elif sex == 1 and edad == 1 and prof==2: #Se puede colcocar tres argumentos?
    print('Es Macri')
elif sex == 2 and prof == 3 and edad == 1:
    print('Es Mirta')
