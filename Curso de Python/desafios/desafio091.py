from random import randint
from time import sleep
from operator import itemgetter
dado = {
    "jogador1":randint(1,6),
    "jogador2":randint(1,6),
    "jogador3":randint(1,6),
    "jogador4":randint(1,6)
}
ranking = []
print("Valores Jogados: ")
for k, v in dado.items():
    print(f"  O {k} jogou o valor {v}")
    sleep(0.5)
ranking = sorted(dado.items(), key=itemgetter(1),reverse=True)
print("=-"*30)
print("  == Ranking dos Jogadores ==")
for i, v in enumerate(ranking):
    print(f"O {i+1} lugar : {v[0]} jogou {v[1]}")
    sleep(0.5)
print("Fim do Programa!")
