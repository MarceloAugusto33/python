nlista= list(range(5))
lista= []
for c in nlista:
    n = float(input("Digite um numero: "))
    lista.append(n)
menor = lista[0]
for c in lista:
    print(c)
    if c < menor:
        menor = c
print(lista)
print(menor)

    
