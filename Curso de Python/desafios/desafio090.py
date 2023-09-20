n = input("Digite Seu nome: ")
m = float(input("Digite sua media: "))
s = ""
if m >= 7:
    s = "Aprovado"
elif m >=5:
    s = "Recuperaçao"
else:
    s = "Reprovado"
aluno = {
    "Nome":n,
    "Media":m,
    "Situaçao":s
}
for k , v in aluno.items():
    print(f"{k} é {v} ")