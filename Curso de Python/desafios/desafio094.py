pessoa = {}
cadastros = []
idades = 0
while True:
    pessoa["Nome"] = str(input("Nome: ")).strip().upper()
    pessoa["Sexo"] = str(input("Sexo[M/F]: ")).strip().upper()[0]
    while pessoa["Sexo"] not in "MF":
        print("Erro!, Digite somente M ou F")
        pessoa["Sexo"] = str(input("Sexo[M/F]: ")).strip().upper()[0]
    pessoa["Idade"] = int(input("Idade: "))
    idades += pessoa["Idade"]
    cadastros.append(pessoa.copy())
    pessoa.clear()
    resp = input("Quer Continuar? [S/N]: ").strip().upper()
    while resp not in "SsNn":
        print("Erro!, Digite somente S ou N")
    if resp in "nN":
        break
media = idades/len(cadastros)
print("=-"*30)
print(f"A) Pessoas Cadastradas: {len(cadastros)}")
print(f"B) A media de idades foi de {media}")
print(f"C) As mulheres cadastradas: ",end=" ")
for p in cadastros:
    if p["Sexo"] in "Ff":
        print(f"{p['Nome']},",end=" ")
print("")
print(f"D) Pessoas acima da media: ")
for p in cadastros:
    if p["Idade"] > media:
        print("")
        for k, v in p.items():
            print(f"{k} = {v} ",end=" ")
        print("")
