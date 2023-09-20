from random import shuffle
p1 = input("Primeiro aluno: ")
p2 = input("Segundo aluno: ")
p3 = input("Terceiro aluno: ")
p4 = input("Quarto aluno: ")
lista_de_alunos = [p1,p2,p3,p4]
shuffle(lista_de_alunos)
print("A ordem de apesentaçao ficou assim: ")
print(lista_de_alunos)