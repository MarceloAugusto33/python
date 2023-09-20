nota1 = float(input("Nota 1 : "))
nota2 = float(input("Nota 2 : "))
media = (nota1+nota2)/2
if media < 5:
    print("Sua media é {}, \033[41mReprovado\033[m".format(media))
elif media >= 5 and media <= 6.9:
    print("Sua media é {} ,\033[43mRecuperaçao\033[m".format(media))
elif media >= 7 and media <=10:
    print("Sua media é {},\033[42mAprovado\033[m".format(media))
