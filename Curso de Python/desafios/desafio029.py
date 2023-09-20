velocidade = float(input("Digite a velocidade do carro: "))
if velocidade > 80:
    print("Voce foi multado: ")
    excesso = velocidade - 80
    multa = excesso * 7 
    print("O valor da multa foi de {:.2f} reais, pois está correndo mais {} km/h acima do limite".format(multa,excesso))

