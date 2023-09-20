Cadastro = []
Pessoas = []
pesados = []
magros = []
while True:
    Pessoas.append(input("Nome: "))
    Pessoas.append(float(input("Peso: ")))
    Cadastro.append(Pessoas[:])
    Pessoas.clear()
    resp = input("Quer continuar: [S/N]")
    if resp in "nN":
        break
print("-"*30)
print(f"Foram cadastradas {len(Cadastro)} pessoas")
print(f"Pessoas mais pesadas: ",end=" ")
for peso in Cadastro:
    if peso[1] >= 100:
        pesados.append(peso)
        print(f"[{peso[0]} = {peso[1]}Kg] ",end="")
print(f"\nPessoas mais leves: ",end="")
for peso in Cadastro:
    if peso[1]<=70:
        magros.append(peso)
        print(f"[{peso[0]} = {peso[1]}Kg]")
    

