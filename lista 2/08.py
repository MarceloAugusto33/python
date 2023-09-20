salario = int(input("Digite seu salario: "))
print(salario)
if salario < 280:
    aum = (20/100)*salario
    print("20%")
    vaum = salario+aum
    print(aum)
    print(vaum)
elif salario >= 280 and salario <700:
    aum = (15/100)*salario
    print("15%")
    vaum = salario+aum
    print(aum)
    print(vaum)
elif salario >=700 and salario < 1500:
    aum = (10/100)*salario
    print("10%")
    vaum = salario+aum
    print(aum)
    print(vaum)
elif salario >= 1500:
    aum = (5/100)*salario
    print("5%")
    vaum = salario+aum
    print(aum)
    print(vaum)


