km = float(input("Quantos km voce percorreu: "))
dias = int(input("Quantos dias voce ficou: "))
custo = (60*dias)+(0.15*km)
print("Voce percorreu {} km e ficou {} dias com o carro, o custo foi de {}R$".format(km,dias,custo))