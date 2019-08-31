dias = int (input("Quantos dias alugados? "))
km = float (input("Quantos km percorridos? "))
preco = (60 * dias) + (0.15 * km)
print ("O Valor de {} dias e {} km é igual a R${:.2f}".format(dias,km,preco))
