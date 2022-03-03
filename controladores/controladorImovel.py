import menu, bancoDeDados, util

def iniciar_sistema_imovel():
    while True:
        menu.imovel()
        op = input("DIGITE OPÇÃO: ")
        if op == "0":
            print("SAINDO DA OP - IMÓVEL")
            break

        elif op == "1":
            print("<<<CADASTRAR IMÓVEL>>>")
            cod = input("DIGITE CÓDIGO: ")
            c = bancoDeDados.buscar_cliente_por_cpf(cod)
            if c == None:
                rua = input("DIGITE RUA: ").upper()
                endereco = input("DIGITE ENDEREÇO: (NÚMERO)")
                bairro = input("DIGITE BAIRRO: ").upper()
                cidade = input("DIGITE CIDADE: ").upper()
                uf = input("DIGITE UF: ").upper()
                imovel = {
                    'codigo':cod,
                    'rua': rua,
                    'endereco': endereco,
                    'bairro': bairro,
                    'cidade': cidade,
                    'uf': uf
                }
                bancoDeDados.adicionar_imovel(imovel)
                print("IMÓVEL CADASTRADO COM SUCESSO!!")

            else:
                print("IMÓVEL JÁ CADASTRADO - TENTE NOVAMENTE")

        elif op == "2":
            cod = input("DIGITE CÓDIGO: ")
            c = bancoDeDados.buscar_imovel_por_codigo(cod)
            if c != None:
                print(c)

            #else:
            #    print("CÓDIGO INVÁLIDO - TENTE NOVAMENTE")

        elif op == "3":
            print("<<<LISTAR TODOS>>>")
            util.imprimir_imoveis()

        else:
            print("OPÇÃO INVÁLIDA - TENTE NOVAMENTE")