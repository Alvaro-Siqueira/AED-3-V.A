import menu, bancoDeDados, util

def iniciar_sistema_cliente():
    while True:
        menu.cliente()
        op = input("DIGITE OPÇÃO: ")
        if op == "0":
            print("SAINDO DA OP - CLIENTE")
            break

        elif op == "1":
            print("<<<CADASTRAR CLIENTE>>>")
            cpf = input("DIGITE CPF: ")
            c = bancoDeDados.buscar_cliente_por_cpf(cpf)
            if c == None:
                nome = input("DIGITE NOME DO CLIENTE: ").upper()
                sexo = input("DIGITE SEXO: [M|-|F]").upper()

                if sexo == "M":
                    sexo = "MASCULINO"
                else:
                    sexo = "FEMININO"

                email = input("DIGITE EMAIL PARA CONTATO: ")
                telefone = input("DIGITE TELEFONE: ")
                cliente = {
                    'cpf': cpf,
                    'nome': nome,
                    'sexo': sexo,
                    'email': email,
                    'telefone': telefone
                }
                bancoDeDados.adicionar_cliente(cliente)
                print("CLIENTE CADASTRADO COM SUCESSO!!")

        elif op == "2":
            cpf = input("DIGITE CPF: ")
            c = bancoDeDados.buscar_cliente_por_cpf(cpf)
            if c != None:
                print(c)
            else:
                print("CPF INVÁLIDO - TENTE NOVAMENTE")

        elif op == "3":
            print("<<<LISTAR POR CPF AVALISTA>>>")
            pass

        elif op == "4":
            util.imprimir_clientes()

        else:
            print("OPÇÃO INVÁLIDA - TENTE NOVAMENTE")
