jogador = {}
time = []
gol = []
partidas = soma = 0
while True:
    jogador["nome"] = str(input("Nome: ")).strip().upper()
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou?: "))
    for partida in range(0,partidas):
        gol.append(int(input(f"Quantos gols na partida {partida+1}?: ")))
    jogador["gols"] = gol[:]
    jogador['total'] = sum(gol)
    time.append(jogador.copy())
    jogador.clear()
    gol.clear()
    resp = input("Quer continuar? [S/N]: ").strip().upper()
    if resp in "Nn":
        break
print("-"*50)
print(f"Cod Nome          Gols    Total")
print("-"*50)
for i , v in enumerate(time):
    print(f"{i}   {v['nome']}       {v['gols']}  {v  ['total']}")
print("-"*50)
while True:
    bucsa = int(input("Digite um numero [999 para parar]: "))
    if bucsa == 999:
        break



print(time)

