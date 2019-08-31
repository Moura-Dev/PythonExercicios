num = int(input('digite um numero inteiro: '))
print('''Escolha uma das bases para conversao:
[ 1 ] converter para Binário
[ 2 ] converter para octal 
[ 3 ] converter para hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif opcao == 2:
    print(' {} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('opcao invalida. tente novamente. ')
