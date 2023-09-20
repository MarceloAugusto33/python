distancia = float(input("Digite a distancia da viagem: "))
if distancia <= 200:
    valor = distancia*0.5
    print("O valor da viagem ficou de {} reais".format(valor))
else:
    valor = distancia*0.45
    print("O valor da viagem ficou de {} reais".format(valor))
