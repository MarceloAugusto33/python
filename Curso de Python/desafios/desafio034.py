salario = float(input("Digite seu slario: "))
if salario > 1.250:
    aumento = salario + (salario*(10/100))
else:
    aumento = salario + (salario*(15/100))
print("Seu novo salario é {} reais".format(aumento))