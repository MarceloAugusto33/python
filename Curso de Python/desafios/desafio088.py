from random import randint
from time import sleep
numeros = []
cartela = []
print("-"*40)
print(F"{'Jogo da Mega cena':^40}")
print("-"*40)
jogos = int(input("Quantos jogos voce quer sortear: "))
for c in range(1,jogos+1):
    for n in range(0,6):
        if n == 0:
            n1 = randint(1,60)
            numeros.append(n1)
        else:
            n1 = randint(1,60)
            while n1 in numeros:
                n1 = randint(1,60)
            numeros.append(n1)
    numeros.sort()
    print(f"Jogo {c}: {numeros}")
    cartela.append(numeros[:])
    numeros.clear()
    sleep(0.5)
print("="*30)
print("Cartelas Sorteadas!Boa sorte")
print(cartela)

  