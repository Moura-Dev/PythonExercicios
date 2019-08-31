# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
# O programa irá perguntar o nome da pessoa.
n = str(input('Digite seu nome: '))
# O programa irá jogar tudo para maiusculo.
n = n.upper()
# O programa irá Caçar a palavra 'SILVA'.
n = str('SILVA' in n)
# O programa irá falar se a pessoa tem 'Silva' no nome ou não.
if n == str('True'):
    print('Seu nome tem Silva.')
else:
    print('Seu nome não tem Silva.')