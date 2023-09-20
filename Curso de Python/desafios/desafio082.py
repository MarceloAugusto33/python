lista = []
pares = []
impares = []
while True:
    n = int(input("Digite um numero: "))
    lista.append(n)
    resp = input("Quer continuar: [S/N]")
    if resp in "Nn":
        break
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)

print(f"Lista de Todos os valores: {lista} com um total de {len(lista)} numeros")
print(f"Listas dos numeros pares: {pares} com um total de {len(pares)}")
print(f"Lista dos numeros Impares: {impares} com um total de {len(impares)}")


    