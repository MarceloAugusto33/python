from random import randint
from time import sleep
numero = randint(0,5)
escolhido = int(input("Adivinhe qual numero escolhido pelo computador: "))
print("O numero que o computador escolheu foi {}".format(numero))
print("Processando...")
sleep(2)
if numero == escolhido:
    print("Voce acertou em cheio!")
else:
    print("Voce errou! Tente novamente!")