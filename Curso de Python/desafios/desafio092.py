import datetime
nome = input("Nome: ")
nascimento = int(input("Nascimento: "))
CTPS = int(input("Carteira de Trabalho(0 nao tem)"))
idade = (datetime.date.today().year) - nascimento
cadastro = {
    "Nome":nome,
    "idade":idade,
    "CTPS":CTPS
}
if CTPS != 0:
    cadastro["contrataçao"] = int(input("Ano de contrataçao: "))
    cadastro["salario"] = int(input("salario: "))
print("=-"*30)
print("== DADOS ==")
for k, v in cadastro.items():
    print(f"O {k} Tem valor {v}")