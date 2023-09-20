boletim = []
aluno = []
media = []
while True:
    nome = input("Nome: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    m = (n1+n2)/2
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    media.append(m)
    boletim.append(aluno[:])
    aluno.clear()
    resp = input("Quer continuar: [S/N]")
    if resp in "Nn":
        break
print("=-"*30)
print("No Nome                Media")
print("-"*30)
for p, pessoa in enumerate(boletim):
    print(f"{p:<}  {pessoa[0]:<20} {media[p]:>.2f}")
print("-"*30)
while True:
    resp = int(input("Mostar nota de Qual aluno[999 para interromper]: "))
    if resp == 999:
        print("Fim do programa!")
        break
    print(f"As notas de {boletim[resp][0]} sao {boletim[resp][1:]}")