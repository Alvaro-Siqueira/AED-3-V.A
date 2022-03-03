import bancoDeDados

def imprimir_clientes():
    print("----CLIENTES----")
    count = 1
    cliente = bancoDeDados.get_clientes()
    for c in cliente:
        print("CLIENTE: ", count)
        print('CPF: ', c.get('cpf'))
        print("NOME: ", c.get('nome'))
        print("SEXO: ", c.get('sexo'))
        print("TELEFONE: ", c.get('telefone'))
        print("---------------")
        count=+1

def imprimir_imoveis():
    print("----IMÓVEIS----")
    count = 1
    imoveis = bancoDeDados.get_clientes()
    for i in imoveis:
        print("IMÓVEL: ",count)
        print('CÓDIGO: ',i.get('codigo'))
        print("RUA: ",i.get('rua'))
        print("ENDEREÇO: ",i.get('endereco'))
        print("BAIRRO: ", i.get('bairro'))
        print("CIDADE: ",i.get('cidade'))
        print("UF: ", i.get('uf'))
        count=+1
        print("---------------")

def imprimir_locacao():
    print("----LOCAÇÕES-----")
    count = 1
    locacao = bancoDeDados.get_locacao()
    for l in locacao:
        print("LOCAÇÃO: ", count)
        print('CÓDIGO: ', l.get('codigo'))
        print("CLIENTE: ", l.get('cliente'))
        print("IMÓVEL: ", l.get('imovel'))
        print("PARCELA: ", l.get('parcela'))
        print("---------------")
        count = +1

def imprimir_parcelas():
    print('----PARCELAS-----')
    count = 1
    parcelas = bancoDeDados.get_parcelas()
    for p in parcelas:
        print("PARCELA: ", count)
        print("PAGAMENTO: ", p.get('pagamento'))
        print("---------------")
        count += 1

