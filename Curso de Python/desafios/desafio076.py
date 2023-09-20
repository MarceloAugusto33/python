produtos = ("Lapis",1.75,"Borracha",2.00,"Caderno",15.9,"estojo",25.00,"Transferidor",4.20,"Compasso",9.99)
print("-"*50)
print("{:^50}".format("Listagem de preços"))
print("-"*50)
for pos in range(0,len(produtos)):
    if pos % 2 == 0:
        print(f"{produtos[pos]:.<30}R$ ",end="")
    else:
        print(f"{produtos[pos]:>10.2f}")