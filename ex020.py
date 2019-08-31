import random
n1 = str (input("digite primeiro nome "))
n2 = str (input("digite segundo nome "))
n3 = str (input ("digite o terceiro nome "))
n4 = str (input ("digite o quarto nome "))
lista = [n1 ,n2 ,n3 , n4]
random.shuffle(lista)
print ("a ordem de apresentação sera")
print (lista)
