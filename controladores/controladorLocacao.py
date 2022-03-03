import menu, bancoDeDados, util

def iniciar_sistema_locacao():
    while True:
        menu.locacao()
        op = input("DIGITE OPÇÃO: ")
        if op == "0":
            print("SAINDO DA OP - LOCAÇÃO")
            break

        elif op == "1":
            util.imprimir_clientes()
            cpf = input("DIGITE CPF: ")
            c = bancoDeDados.buscar_cliente_por_cpf(cpf)

            if c != None:
                util.imprimir_imoveis()
                codImovel = input("DIGITE O CÓDIGO IMÓVEL: ")
                i = bancoDeDados.buscar_imovel_por_codigo(codImovel)

                if i != None:
                    util.imprimir_parcelas()
                    codParcela = input("DIGITE CÓDIGO DA PARCELA: ")
                    p = bancoDeDados.buscar_parcela_por_codigo(codParcela)

                    if p != None:
                        codLocacao = input("DIGITE CÓDIGO DA LOCAÇÃO: ")
                        l = bancoDeDados.buscar_locacao_por_codigo(codLocacao)

                        if l == None:
                            locacao = {
                                'codigo': l,
                                'cliente': c,
                                'imovel': i,
                                'parcela': p
                            }
                            bancoDeDados.adicionar_locacao(locacao)
                            print("LOCAÇÃO CADASTRADA COM SUCESSO!!")

                        else:
                            print("LOCAÇÃO JÁ CADASTRADA - TENTE NOVAMENTE!")
                else:
                    print("IMÓVEL NÃO EXISTENTE - TENTE NOVAMENTE")

            else:
                print("CLIENTE NÃO ENCONTRADO - TENTE NOVAMENTE")

        elif op == "2":
            print("<<<BUSCAE LOCAÇÃO POR CÓDIGO>>>")
            codlocacao = input("DIGITE CÓDIGO DA VENDA: ")
            cod = bancoDeDados.buscar_locacao_por_codigo(codlocacao)
            if cod != None:
                print(cod)

            else:
                print("CÓDIGO INVÁLIDO - TENTE NOVAMENTE")


        elif op == "3":
            print("<<<BUSCAR POR CPF AVALISTA>>>")
            pass

        elif op == "4":
            print("<<<LISTAR PARCELAS>>>")
            util.imprimir_parcelas()

        else:
            print("OPÇÃO INVÁLIDA - TENTE NOVAMENTE!!")
