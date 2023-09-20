aprv = {}
gols = []
gol = totalg = 0
aprv["Nome"] = str(input("Nome: "))
qntd = int(input(f"Quantas Partidas {aprv['Nome']} jogou: "))
for jogos in range(0,qntd):
    gol = int(input(f"Quantos gols na partida {jogos+1}: "))
    totalg += gol
    gols.append(gol)
aprv["gols"] = gols[:]
aprv["total"] = totalg
print("-="*30)
for k,v in aprv.items():
    print(f"O campo {k} tem valor {v}")
print("-="*30)
print(f"{aprv['Nome']} jogou {qntd} partidas")
for c in range(0,qntd):
    print(f"Na partida {c+1}, fez {gols[c]} gols")
print(f"Total de gols = {totalg}")



