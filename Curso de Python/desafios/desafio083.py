abre = fecha = 0
exp = input("Digite uma expresao matematica: ")
for c in exp:
    if c == "(":
        abre += 1
    if c == ")":
        fecha += 1
if abre == fecha:
    print("\033[42mExpresao valida!\033[m")
else:
    print("\033[41mExpressao invalida!\033[m")
print(exp)