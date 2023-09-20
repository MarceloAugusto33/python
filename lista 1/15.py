gh = int(input("Quanto voce ganha por hora: "))
h = int(input("Quantas horas voce trabalha: "))
sal = (gh*h)*30
print(sal)
imp_renda = (11/100)*sal
imp_INSS = (8/100)*sal
imp_SIND = (5/100)*sal
sal_liquido = (sal-imp_renda-imp_INSS-imp_SIND)
print(sal)
print(imp_INSS)
print(imp_SIND)
print(sal_liquido)
print("-------------------------------")