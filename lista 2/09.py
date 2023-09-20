gh = int(input("Digite Quanto voce ganha por hora: "))
h = int(input("Quantas horas voce trabalha: "))
salario = (gh*h)*30
imp_sind = (3/100)*salario
FGTS = (11/100)*salario
if salario <=900:
    print("isento")
    imp_renda=0
    salario_novo = salario+FGTS
    print("Salario Bruto: R$"+str(salario))
    print("(-) SINDICATO: R$" +str(imp_sind))
    print("FGTS (11%): R%"+str(FGTS))
    print("Total de descontos: R$"+str(imp_renda+imp_sind))
    print("Salario Liquido: R$" +str(salario_novo))
elif salario <= 1500:
    imp_renda= (5/100)*salario
    salario_novo=(salario+FGTS-imp_renda-imp_sind)
    print("Salario Bruto: R$"+str(salario))
    print("(-) SINDICATO: R$" +str(imp_sind))
    print("FGTS (11%): R%"+str(FGTS))
    print("Total de descontos: R$"+str(imp_renda+imp_sind))
    print("Salario Liquido: R$" +str(salario_novo))
elif salario <= 2500:
    imp_renda= (10/100)*salario
    salario_novo=(salario+FGTS-imp_renda-imp_sind)
    print("Salario Bruto: R$"+str(salario))
    print("(-) SINDICATO: R$" +str(imp_sind))
    print("FGTS (11%): R%"+str(FGTS))
    print("Total de descontos: R$"+str(imp_renda+imp_sind))
    print("Salario Liquido: R$" +str(salario_novo))
elif salario >2500:
    imp_renda= (20/100)*salario
    salario_novo=(salario+FGTS-imp_renda-imp_sind)
    print("Salario Bruto: R$"+str(salario))
    print("(-) SINDICATO: R$" +str(imp_sind))
    print("FGTS (11%): R%"+str(FGTS))
    print("Total de descontos: R$"+str(imp_renda+imp_sind))
    print("Salario Liquido: R$" +str(salario_novo))

