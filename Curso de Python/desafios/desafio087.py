matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = somap = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = (int(input(f"Digite um valor para[{l}, {c}]: ")))
for l in range(0,3):
    for c in range(0,3):
        print(f"[  {matriz[l][c]}  ]",end=" ")
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        if c == 2:
            soma += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                if matriz[l][c] > maior:
                    maior = matriz[l][c]

    print()
print("="*30)
print(f"A soma dos valores pares é {somap}")
print(f"A soma dos valores da terceira coluna: {soma}")
print(f"O maior valor da segunda linha é {maior}")
