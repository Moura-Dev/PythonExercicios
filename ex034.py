from time import sleep

s = int(input('Quanto você ganha atualmente? R$'))  # s recebe o salário de um funcionário.

print('CALCULANDO O SEU AUMENTO...\n')
sleep(3)

# Verifica se o salário é maior do que 1250, se for o aumento será de 10%, caso não seja, o aumento será de 15%
if s > 1250:
    aumento = s + ((s * 10) / 100)
    print(f'O seu antigo salário era R${s:.2f}\n'
          f'Com um aumento de 10% passará a ser R${aumento:.2f}')
else:
    aumento = s + ((s * 15) / 100)
    print(f'O seu antigo salário era R${s:.2f}\n'
          f'Com um aumento de 15% passará a ser R${aumento:.2f}')

print('\nContinue fazendo esse incrível trabalho!')