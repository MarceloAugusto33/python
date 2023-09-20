total_idade = 0
menor_de_20_Mulher = 0
nome_mais_velho = str
for contatos in range(1,5):
    nome = str(input("Nome: ")).strip().upper()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: ")).strip().upper()
    print("-=-"*5)
    total_idade += +idade
    if sexo == "MASCULINO":
        if contatos == 1:
            velho = idade
            nome_mais_velho = nome
        else:
            if idade > velho:
                velho = idade
                nome_mais_velho = nome
    if sexo == "FEMININO":
        if idade < 20:
            menor_de_20_Mulher += 1
media = total_idade/4
print('''======================
DADOS PESSOAS: 
MEDIA DE IDADE: {}
NOME DA PESSOA MAIS VELHA: {}
QUANTAS MULHERES TEM MENOS DE 20 ANOS: {}'''.format(media,nome_mais_velho,menor_de_20_Mulher))


    

