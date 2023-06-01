#Arthur Sabino & Gustavo muzel
print("\n<Agenda telefonica>")
print("!Versão free!")
contatos = [[] for log in range(999)] #Limite de armazenamento de dados = 999 (versão free)

while True: #Menu de operações
    print("\n--Menu e suas opções-- \n1. <Adicionar contato e seus dados> \n2. <Exclusão de um contato> \n3. <Listar todos os contatos e seus dados> \n4. <Modificar dados de um contato> \n5. <Listar dados de um contato> \n6. <Finalizar sessão>")
    op = input("<Selecione a operação que deseja: ") #Seleção de uma operação
    if op == "1": #Opção de numero 1 selecionada, Adição de um contato e seus dados
        for i, contato in enumerate(contatos):
            if not contato:
                nome = input("\n<Digite o nome do contato: ")
                telefone = input("<Digite o telefone do contato: ")
                empresa = input("<Digite a empresa onde trabalha: ")
                contatos[i] = [nome, telefone, empresa]
                print("Contato adicionado a lista.")
                break
        else:
            print("\n<A lista de contatos está cheia... \n<Exclua um contato para continuar... \n<Ou pague a versão premium para mais espaço de armazenamento.")

    elif op == "2": #Opção de numero 2 selecionada, Exclusão de um contato selecionado pelo usuario.
        nome = input("\nDigite o nome do contato para sua exclusão: ")
        for i, contato in enumerate(contatos):
            if contato and contato[0] == nome:
                contatos[i] = []
                print("Contato removido.")
                break
        else:
            print("Contato inexistente.")

    elif op == "3": #Opção de numero 3 selecionada, Listar todos os contatos e seus dados.
        print("\nLista de todos os contatos e seus dados:")
        for contato in contatos:
            if contato:
                print("Nome:", contato[0] )
                print("Telefone:", contato[1])
                print("Empresa:", contato[2])
                print("--------------------")

    elif op == "4": #opção de nu mero 4 selecionada, Alteração de dados de um contato definido pelo usuario.
        nome = input("\n<Alteração de dados... \n<Digite o nome do contato a ser modificado: ")
        for i, contato in enumerate(contatos):
            if contato and contato[0] == nome:
                telefone = input("<Digite o telefone: ")
                empresa = input("<Digite a empresa: ")
                contatos[i][1] = telefone
                contatos[i][2] = empresa
                print("<Dados do contato alterado.")
                break
        else:
            print("Contato inexistente.")

    elif op == "5": #Opção de numero 5 selecionada, Listar dados de um contato selecionado pelo usuario.
        nome = input("\nDigite o nome do contato para listar seus dados: ")
        for contato in contatos:
            if contato and contato[0] == nome:
                print("Nome:", contato[0])
                print("Telefone:", contato[1])
                print("Empresa:", contato[2])
                break
        else:
            print("<Contato inexistente.")

    elif op == "6": #Opção de numero 6 selecionada, Finalizar sessão
        print("\nFinalizando sessão....\nBYE BYE :( ")
        break

    else:
        print("!Apenas numeros de 1 a 6 permitidos!")