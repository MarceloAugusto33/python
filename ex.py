l = []
print(l)
print("Podemos adicionar um item ao final da lista: com o codigo = variavel.append(item novo)")
l.append(20)
l.append("jessa")
l.append(35.75)
l.append([30,60,90])
l.append("Marcelo")
print(l)
print("Podemos ver o tamanho da lista: com o codigo = len(variavel)")
print("existe", len(l) ,"itens nessa lista")
print("Inserir itens em um lugar especifico: codigo = variavel.insert(posiçao, item novo )")
l.insert(5, "Augusto")
print(l)
print("Remover valores e excluir o primeiro a aparecer: codigo = variavel.remove(Item)")
l.remove("Augusto")
print(l)
print("Remover um valor em um lugar especifico: Codigo = variavel.pop( len( variavel ) -1 )")
l.pop(len(l)-1)
print(l)