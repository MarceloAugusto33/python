from time import sleep
from random import choice
print('''Suas opçoes:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogada = int(input("Oque voce vai jogar: "))
lista = ["pedra","papel","tesoura"]
jogada_maquina = choice(lista).upper()
sleep(1)
print("Jo")
sleep(1)
print("ken")
sleep(1)
print("po")
if jogada == 1:
    if "PEDRA" == jogada_maquina:
        print('''====================
computador jogou {}
jogador jogou {}
===================='''.format(jogada_maquina,"PEDRA"))
        print("\033[43mEmpate!\033[m")
    elif "PAPEL" == jogada_maquina:
        print('''====================
computador jogou {}
jogador jogou {}
===================='''.format(jogada_maquina,"PEDRA"))
        print("\033[41mMAQUINA GANHOU!\033[m")
    elif "TESOURA" == jogada_maquina:
        print('''====================
computador jogou {}
jogador jogou {}
===================='''.format(jogada_maquina,"PEDRA"))
        print("\033[42mJOGADOR GANHOU!\033[m")
elif jogada == 2:
    if "PEDRA" == jogada_maquina:
        print('''====================
computador jogou {}
jogador jogou {}
===================='''.format(jogada_maquina,"PAPEL"))
        print("\033[42mJOGADOR GANHOU!\033[m")
    elif "PAPEL" == jogada_maquina:
        print('''====================
computador jogou {}
jogador jogou {}
===================='''.format(jogada_maquina,"PAPEL"))
        print("\033[43mEMPATE!\033[m")
    elif "TESOURA" == jogada_maquina:
        print('''====================
computador jogou {}
jogador jogou {}
===================='''.format(jogada_maquina,"PAPEL"))
        print("\033[41mMAQUINA GANHOU!\033[m")
elif jogada == 3:
    if "PEDRA" == jogada_maquina:
        print('''====================
computador jogou {}
jogador jogou {}
===================='''.format(jogada_maquina,"TESOURA"))
        print("\033[41mMAQUINA GANHOU!\033[m")
    elif "PAPEL" == jogada_maquina:
        print('''====================
computador jogou {}
jogador jogou {}
===================='''.format(jogada_maquina,"TESOURA"))
        print("\033[42mJOGADOR GANHOU!\033[m")
    elif "TESOURA" == jogada_maquina:
        print('''====================
computador jogou {}
jogador jogou {}
===================='''.format(jogada_maquina,"TESOURA"))
        print("\033[43mEMPATE!\033[m")
else:
    print("\033[41mComando Invalido!\033[m")