termo1 = int(input("Digite o primeiro termo"))
razao = int(input("Qual é a razao: "))
lista = []
for c in range(termo1,razao*10+1,razao):
    lista.append(c)
print(lista)