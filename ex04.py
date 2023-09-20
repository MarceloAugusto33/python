pA= 80.000
tA = 3/100
pB = 200.000
tB = 1.5/100
anos = 0
while pA <= pB:
    aumA= pA*tA
    pA= aumA+pA

    aumB= pB*tB
    pB = aumB+pB

    anos = anos + 1
print(anos)