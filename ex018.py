import math
angulo = float (input("digite o angulo que voce deseja: "))
seno = math.sin(math.radians(angulo))
print ("o Angulo de {} tem o seno de {:.2f}".format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print ("O Angulo de {} tem o cosseno {:.2f} ".format(angulo, cosseno))

tangente = math.tan(math.radians(angulo))
print ("O angulo de {} tem a tangente {:.2f}".format(angulo, tangente))