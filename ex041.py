from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Classificação Mirim')
elif   idade <= 14 and idade > 9:
    print('Classificação Infantil')
elif idade <=19 and idade > 14:
    print('Classificação Junior')
elif idade <= 25 and idade > 19:
    print('Classificação Senior')
elif idade > 25:
    print('Categoria Master')
