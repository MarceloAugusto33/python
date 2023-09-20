soma = contador = 0
op = "S"
while op == "S":
    n = int(input("Digite um numero: "))
    op = str(input("Quer continuar: [S]/[N]")).strip().upper()[0]
    while op != "S" and op != "N":
        print("Comando invalido!")
        n = int(input("Digite um numero: "))
        op = str(input("Quer continuar: [S]/[N]")).strip().upper()[0]
    soma += n
    contador += 1
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma/contador  
print("Media: {:.2f}".format(media))
print("Quantidade de nº: {}".format(contador))
print("Maior numero: {}".format(maior))
print("Menor numero: {}".format(menor))