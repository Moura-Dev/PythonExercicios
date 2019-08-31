print('preços:')
print('0,50 ate 200 km')
print('0,45 maisde 200 km')
n1=int(input('qual a distancia da viajem que voce quer fazer?'))
if n1<= 200 or n1==200:
    n2=(n1*50)/100
    print('para uma viajem de {}.km voce vai pagar {}'.format(n1,n2))
else:
    n3=(n1*45)/100
    print('para uma viagem de {}.km voce vai pagar {}'.format(n1,n3))