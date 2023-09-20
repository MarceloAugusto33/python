n1 = float(input("Digite o preço do produto: ")) 
n2 = float(input("Digite o preço do produto: ")) 
n3 = float(input("Digite o preço do produto: "))
if n1<n2 and n1<n3:
    print(n1)
elif n2<n3 and n2<n1:
    print(n2)
elif n3<n1 and n3<n1:
    print(n3)