menor = 0
maior = 0
for c in range(1,6):
    peso = int(input("Qual seu peso: "))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(maior)
print(menor)