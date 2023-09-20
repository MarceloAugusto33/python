from datetime import date
pessoas = 0
atual = date.today().year
maiores = 0
menores = 0
for c in range(0,7):
    nascimento = int(input("Digite em que ano voce nasceu: "))
    if (atual - nascimento) < 21:
        menores = menores + 1
    elif (atual - nascimento) >= 21:
        maiores = maiores + 1
print("Quantidade Pessoas que ja sao maiores de 21 anos: {}".format(maiores))
print("Quantidade de Pessoas que nao tem mais de 21 anos: {}".format(menores))

