n=int((input(('digite o número para ser feita a leitura de Par ou Impar:'))))
n1=n/2
n2=str(n1)
n3='.5' in n2
if n3 == True:
    print(' O número {} è Ìmpar.'.format(n))

else:
    print('O número é {} Par.'.format(n))