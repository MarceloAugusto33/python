from random import randint
escolha_computador = randint(0,10)
escolha_jogador = int(input("Tente adivinhar o numero que a maquina escolheu: "))
jogadas = 0
while escolha_computador != escolha_jogador:
    print("Errou!, tente novamente")
    escolha_jogador = int(input("Tente adivinhar o numero que a maquina escolheu: "))
    jogadas += 1
print("Acertou")
print("jogadas {}".format(jogadas))
