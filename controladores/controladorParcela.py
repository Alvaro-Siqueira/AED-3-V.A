import menu, bancoDeDados, util

def iniciar_sistema_parcela():
    while True:
        menu.parcela()
        op = input("DIGITE OPÇÃO: ")
        if op == "0":
            print("SAINDO DA OP - PARCELAS")
            break

        elif op == "1":
            print("<<<CADASTRAR PARCELA>>>")
        codParcela = input("DIGITE CÓDIGO DA PARCELA: ")
        p = bancoDeDados.buscar_parcela_por_codigo(codParcela)
        if p == None:
            pagamento = False
            valorParcela = float(input("DIGITE VALOR DA PARCELA: "))
            parcela = {
                'pagamento': pagamento,
                'valor_parcela': valorParcela,
                'codigo': codParcela
            }
            bancoDeDados.adicionar_parcela(parcela)
            print("PARCELA CADASTRADA COM SUCESSO!!")

        elif op == "2":
            print("<<<PAGAR PARCELA>>>")
            parcela['status'] = not parcela.get('status')
            print("PARCELA PAGA COM SUCESSO!!")

        elif op == "3":
            codParcela = input("DIGITE CÓDIGO DA PARCELA: ")
            p = bancoDeDados.buscar_parcela_por_codigo(codParcela)
            if p != None:
                print(p)

        elif op == "4":
            util.imprimir_parcelas()