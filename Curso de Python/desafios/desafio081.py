lista = []
while True:
    n = int(input("Digite um numero: "))
    lista.append(n)
    op = input("Quer continuar: [S/N]").strip().upper()
    while op != "N" and op != "S":
        op = input("Quer continuar: [S/N]").strip().upper()
    if op in "Nn":
        print("Fim do Programa!")
        break
lista.sort(reverse=True)
print(f"Valores adicionados: {lista}")
print(f"numers digitados: {len(lista)}")
if 5 in lista:
    print("O numero 5 foi encontrado na lista!")
else:
    print("O numero 5 nao foi encontrado na lista!")

    