vel = float(input('Qual a velocidade atual do carro?: '))
multa = (vel - 80) * 7
if vel <= 80:
    print('Sua velocudade está dentro do limite permitido que é de 80km continue assim, dirija com cuidado')
else:
    print('VOCÊ FOI MULTADO POR ULTRAPASSAR O LIMITE PERMITIDO DE VELOCIDADE QUE É DE 80 KM E TERÁ QUE PAGAR {}'.format(multa))