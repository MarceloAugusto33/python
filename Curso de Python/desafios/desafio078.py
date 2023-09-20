lista = []
cont = 0
for c in range(0,5):
    lista.append(int(input(f"Digite um numero na posiçao {c}: ")))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f"Numeros digitados: {lista}")
print(f"Maior numero: {maior} nas posiçoes ",end="")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i+1} ",end=" ")
print(f"\nMenor numero: {menor} nas posiçoes ",end="")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i+1} ",end=" ")


