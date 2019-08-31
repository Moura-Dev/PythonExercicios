salario = float (input("Qual o salario atual: R$"))
calc = salario * 15 / 100
reaj = salario + calc
print ("Seu Salario Atual é {:.2f} e com reajuste fica {:.2f}".format(salario,reaj))