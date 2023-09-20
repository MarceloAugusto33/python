def opcao1():
    print("-----------------------------")
    print("|          Agenda           |")
    print("-----------------------------")
    print(" ")
    print(" [1] Incluir novo Contato")
    print(" [2] Bucar Contato")
    print(" [3] Editar Contato")
    print(" [4] Excluir Contato")
    print(" [5] Todos os Contatos")
    print(" [6] Sair")
    print("")
    print("Lista de Contatos: ", Total_Contatos)
def incluirContato():
    print("- [1] Incluir novo Contato")
    nome = input("Digite o nome: ")
    email = input("Digite o Email: ")
    telefone = input("Digite o Telefone:")
    add_contato = {
    "Nome":nome,
    "email":email,
    "telefone":telefone
    }
    Total_Contatos.append(add_contato)
    print("")
    print("----------------------------------------------------")
    print("Contato adicionado: ",add_contato)
def BuscarContato():
    if len(Total_Contatos) == 0:
        print("")
        print("----------------------------------------------------")
        print("Nenhum Contato adicionado a lista!")
    else:
        print("- [2] Bucar Contato")
        pesquisar = input("buscar por Nome [N], Email [E], Telefone [T]: ")
        if pesquisar == "N" or pesquisar =="n":
            pesquisar_nome = input("Digite o Nome: ")
            for contatos in Total_Contatos:
                if pesquisar_nome in contatos["Nome"]:
                    print("")
                    print("----------------------------------------------------")
                    print("Contato encontrado: ")
                    print(contatos)
        if pesquisar == "E" or pesquisar =="e":
            pesquisar_Email = input("Digite o Email: ")
            for contatos in Total_Contatos:
                if pesquisar_Email in contatos["email"]:
                    print("")
                    print("----------------------------------------------------")
                    print("Contato encontrado: ")
                    print(contatos)
        if pesquisar == "T" or pesquisar =="t":
            pesquisar_Telefone = input("Digite o Telefone: ")
            for contatos in Total_Contatos:
                if pesquisar_Telefone in contatos["telefone"]:
                    print("")
                    print("----------------------------------------------------")
                    print("Contato encontrado: ")
                    print(contatos)
def EditarContato():
    if len(Total_Contatos) == 0:
        print("")
        print("----------------------------------------------------")
        print("Nenhum Contato adicionado a lista!")
    else:
        print("Contatos: ",Total_Contatos)
        print("- [3] Editar Contato")
        editar_Contato = input("Digite o nome do contato que voce quer editar: ")
        for contatos in Total_Contatos:
            if editar_Contato in contatos["Nome"]:
                pesquisar = input("Voce quer Editar Nome [N], Editar Email [E], Editar Telefone [T]: ")
                if pesquisar == "N" or pesquisar =="n":
                    if editar_Contato in contatos["Nome"]:
                        contatos["Nome"] = input("Novo nome: ")
                        print("")
                        print("----------------------------------------------------")
                        print("Nome alterado :", contatos,"!")
                if pesquisar == "E" or pesquisar =="e":
                    pesquisar_Email = input("Digite o email do contato: ")
                    if pesquisar_Email in contatos["email"]:
                        contatos["email"] = input("Novo email: ")
                        print("")
                        print("----------------------------------------------------")
                        print("Email alterado :", contatos,"!")
                if pesquisar == "T" or pesquisar =="t":
                    pesquisar_Telefone = input("Digite o Telefone do contato: ")
                    if pesquisar_Telefone in contatos["telefone"]:
                        contatos["telefone"] = input("Novo telefone: ")
                        contatos["telefone"] = int(contatos["telefone"])
                        print("")
                        print("----------------------------------------------------")
                        print("Telefone alterado :", contatos,"!")
def Excluircontato():
    if len(Total_Contatos) == 0:
        print("Nenhum Contato adicionado a lista!")
    else:
        print("Contatos: ", Total_Contatos)
        print("- [4] Excluir Contato")
        pesquisar = input("Voce quer excluir por Nome [N], Editar Email [E], Editar Telefone [T]: ")
        if pesquisar == "N" or pesquisar =="n":
            pesquisar_nome = input("Digite o nome do contato Que voce quer excluir: ")
            for contatos in Total_Contatos:
                if pesquisar_nome in contatos["Nome"]:
                    print("")
                    print("----------------------------------------------------")
                    print("Contato com o nome", pesquisar_nome,"foi removido!")
                    Total_Contatos.remove(contatos)
                    print("Nova Lista de Contatos: ")
                    return Total_Contatos
        if pesquisar == "E" or pesquisar =="e":
            pesquisar_Email = input("Digite o email do contato: ")
            for contatos in Total_Contatos:
                if pesquisar_Email in contatos["email"]:
                    print("")
                    print("----------------------------------------------------")
                    print("Contato com o email", pesquisar_Email,"foi removido!")
                    Total_Contatos.remove(contatos)
                    print("Nova Lista de Contatos: ")
                    return Total_Contatos
        if pesquisar == "T" or pesquisar =="t":
            pesquisar_Telefone = input("Digite o Telefone do contato: ")
            for contatos in Total_Contatos:
                if pesquisar_Telefone in contatos["telefone"]:
                    print("")
                    print("----------------------------------------------------")
                    print("Contato com o telefone", pesquisar_Telefone,"foi removido!")
                    Total_Contatos.remove(contatos)
                    print("Nova Lista de Contatos: ")
                    return Total_Contatos
def todosContatos():
    if len(Total_Contatos) == 0:
        print("Nenhum contato adicionado!")
    else:
        print("- [5] Todos os Contatos")
        contador = 0
        print("")
        print("----------------------------------------------------")
        for contatos in Total_Contatos:
            contador = contador + 1
            print("Contato:", contador)
            print(contatos)
Total_Contatos = []
opcao = 0
index = 0
contador = 0
while opcao != 6:
    opcao1()
    opcao = input("Digite a opçao: ")
    opcao = int(opcao)
    print("")
    while opcao < 1 or opcao > 6:
        print("Digite somente as numeraçoes acima!!")
        opcao = input("Digite a opçao: ")
        opcao = int(opcao)
        print("")
    if opcao == 1:
        op1 = incluirContato()
        print(op1)
    elif opcao == 2:
        op2 = BuscarContato()
        print(op2)
    elif opcao == 3:
        op3 = EditarContato()
        print(op3)
    elif opcao == 4:
        op4 = Excluircontato()
        print(op4)
    elif opcao == 5:
        op5 = todosContatos()
        print(op5)
print("Agenda finalizada")