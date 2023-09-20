def exibirmensagem(nome):
    print("Bem vindo ", nome)
    return "Foi facil"
nome = input("Digite seu nome: ")
mensagem = exibirmensagem(nome)
print(mensagem)