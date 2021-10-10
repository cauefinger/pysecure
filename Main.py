senhaCorreta = "segredo"
tentativas = 3
autenticado = False
senhas = []

while tentativas > 0:
    senha = input("Insira a senha: ")
    if senhaCorreta == senha:
        print("Senha correta")
        autenticado = True
        tentativas = 0
    else:
        print("Senha errada")
        tentativas -= 1

if autenticado:
    print("Bem vindo! Escolha sua opção: ")
    while True:
        print("1 - Inserir nova senha")
        print("2 - Ver senhas ")
        print("3 - Excluir senha ")
        print("4 - Finalizar programa")
        opcao = int(input())

        if opcao == 1:
            titulo = input("Insira de onde é essa senha: ")
            senhaAdicionada = input("Insira a senha: ")
            senhas.append([titulo, senhaAdicionada])
            print("Senha adicionada.")

        if opcao == 2:
            for senha in senhas:
                print("Descrição: " + senha[0])
                print("Senha: " + senha[1])

        if opcao == 4:
            exit()
