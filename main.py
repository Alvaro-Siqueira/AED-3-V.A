import menu
from controladores import controladorCliente, controladorImovel, controladorLocacao, controladorParcela

def iniciar_sistema():
    while True:
        menu.principal()
        op = input("DIGITE OPÇÃO: ")

        if op == "0":
            print("SAINDO DO SISTEMA!")
            break

        elif op == "1":
            "CLIENTE"
            controladorCliente.iniciar_sistema_cliente()

        elif op == "2":
            "IMÓVEL"
            controladorImovel.iniciar_sistema_imovel()

        elif op == "3":
            "PARCELAS"
            controladorParcela.iniciar_sistema_parcela()

        elif op == "4":
            "LOCAÇÃO"
            controladorLocacao.iniciar_sistema_locacao()

        else:
            print("OPÇÃO INVÁLIDA - TENTE NOVAMENTE!")

iniciar_sistema()

