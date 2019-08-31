frase = str(input('Digite uma frase: ')).strip().lower().replace(' ',"").replace('ã','a').replace('á','a').replace('à','a').replace('â','a')
print('A letra "A" aparece na frase {} vezes'.format(frase.count('a')))
print('A letra "A" aparece pela primeira vez na {}° posição'.format(frase.find('a') + 1))
print('A letra aparece "A" aparece na frase pela última vez na posição {}'.format(frase.rfind('a')+1))