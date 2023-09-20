from datetime import date
ano = int(input("Qual ano: "))
if ano == 0:
    print(date.today().year)
if (ano % 4) == 0 and ano % 100 != 0:
    print("ano bissexto")
else:
    print("nao é ano bissexto")

