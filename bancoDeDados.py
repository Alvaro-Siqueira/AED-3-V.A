__banco_de_dados = {
    'clientes':[],
    'imoveis':[],
    'locacoes':[],
    'parcelas':[]
}

def adicionar_cliente(cliente):
    __banco_de_dados['clientes'].append(cliente)

def buscar_cliente_por_cpf(cpf):
       cliente = __banco_de_dados.get('clientes')
       for c in cliente:
           if c.get('cpf') == cpf:
               return c
       return None

def get_clientes():
    return __banco_de_dados.get('clientes').copy()

def buscar_imovel_por_codigo(codigo):
    imovel = __banco_de_dados.get('imoveis')
    for i in imovel:
        if i.get('codigo') == codigo:
            return i
    return None

def adicionar_imovel(imovel):
    __banco_de_dados['imoveis'].append(imovel)

def get_imovel():
    return __banco_de_dados.get('imoveis').copy()

def buscar_locacao_por_codigo(codigo):
    locacao = __banco_de_dados.get('locacao')
    for l in locacao:
        if l.get('codigo') == codigo:
            return l
    return None

def adicionar_locacao(locacao):
    __banco_de_dados['locacoes'].append(locacao)

def get_locacao():
    return __banco_de_dados.get('locacoes').copy()

def buscar_parcela_por_codigo(codigo):
    parcela = __banco_de_dados.get('parcelas')
    for p in parcela:
        if p.get('codigo') == codigo:
            return p
    return None

def adicionar_parcela(parcela):
    __banco_de_dados['parcelas'].append(parcela)

def get_parcelas():
    return  __banco_de_dados.get('parcelas').copy()