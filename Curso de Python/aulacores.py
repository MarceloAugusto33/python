estado = {}
brasil = []
for c in range(0,3):
    estado["uf"] = str(input("unidade federativa: "))
    estado["sigla"] = str(input("Sigla do estado: "))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v)
        