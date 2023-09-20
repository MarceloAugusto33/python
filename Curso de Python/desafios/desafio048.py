soma = 0
for c in range(1, 501):
    if (c % 2) != 0 and c % 3 == 0:
        soma= soma + c
print("Fim da contagem")
print("A soma dos valores : {}".format(soma))