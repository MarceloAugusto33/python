import datetime
nascimento = int(input("Em que ano voce nasceu: "))
ano_atual = datetime.date.today().year
idade = ano_atual - nascimento
if idade <= 17:
    print("Voce ainda nao pode se alistar!")
    tempo = 18 - idade
    print("Falta {} anos para voce se alistar!".format(tempo))
elif idade == 18:
    print("Este é o momento exato para voce se alistar!!!!!")
else:
    print("O seu alistamento ja passou!")
    tempo = idade - 18
    print("O seu alistamento ja passou ha {} anos".format(tempo))