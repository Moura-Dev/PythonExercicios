n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
media = float (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f} , a media do aluno é {:.1f} '.format(n1 , n2, media))
if media  >=5 and media <7:
    print('Recuperação')
elif media > 7:
    print('Aprovado')
else:
    media < 5
    print('Reprovado')


