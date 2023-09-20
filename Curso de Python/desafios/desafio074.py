from random import randint
cont = 0
tupla = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
for c in tupla:
    cont +=1
    if cont == 1:
        maior = c
        menor = c
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
print(f"Valores sorteados {tupla}")
print(f"Maior valor sorteado foi {maior}")
print(f"Menor valor sorteado foi {menor}")
