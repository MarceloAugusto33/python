lista = []
while True:
    n = int(input("Numero: "))
    if n in lista:
        print("\033[47mvalor duplicado!, Nao vou adicionar\033[m1")
    else:
        lista.append(n)
        print("\033[42mValor Adicionado na lista!\033[m")
    op = ""
    while op != "S" and op != "N":
        op = input("Quer Continuar: [S] [N]").strip().upper()
    if op == "N":
        break
lista.sort()
print(f"Voce digitou os valores {lista}")
    