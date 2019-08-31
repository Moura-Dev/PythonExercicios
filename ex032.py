from datetime import date

ano = int(input('Digite um ano qualquer (Digite 0 para analisar o ano atual: '))


if ano == 0:

    ano = date.today().year


if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

    resultado = str('')

else:

    resultado = str('não ')


print('O ano {} {}é um ano bissexto e, consequentemente, fevereiro desse ano {}tem 29 dias.'.format(ano, resultado, resultado))