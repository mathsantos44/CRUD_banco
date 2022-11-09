import re

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)

pessoa = {}

continuar = True

while continuar == True:
    print("1 - Incluir")
    print("2 - Alterar")
    print("3 - Exibir")
    print("4 - Excluir")
    print("0 - Sair")
    opcao = input("Digite a opção que você deseja: ").strip()

    if is_int(opcao):
        opcao = int(opcao)

        if opcao >= 0 and opcao <= 4:
            digCerto = True
        else:
            digCerto = False

        while not digCerto:
            opcao = input("Você digitou uma opção inválida, tente novamente: ").strip()

            if is_int(opcao):
                opcao = int(opcao)

                if opcao >= 0 and opcao <= 4:
                    digCerto = True
                    break
                else:
                    digCerto = False
            else:
                digCerto = False
    else:
        digCerto = False

        while not digCerto:
            opcao = input("Você digitou uma opção inválida, tente novamente: ").strip()

            if is_int(opcao):
                opcao = int(opcao)

                if opcao >= 0 and opcao <= 4:
                    digCerto = True
                    break
                else:
                    digCerto = False
            else:
                digCerto = False

    if opcao == 1:
        nome = input("Digite o nome: ").strip()
        cpf = input("Digite o CPF: ").strip()
        idade = input("Digite a idade: ").strip()
        if is_int(idade):
            idade = int(idade)
        else:
            idadeFalse = False

            while not idadeFalse:
                idade = input("Por favor, digite a idade em números: ").strip()

                if is_int(idade):
                    idadeFalse = True
                    idade = int(idade)
                    break
        endereco = input("Digite o endereço: ").strip()
        limite = input("Digite o Limite de Crédito: ").strip()
        if is_number(limite):
            limite = float(limite)
        else:
            limiteFalso = False

            while not limiteFalso:
                limite = input("Digite o limite apenas com números: ").strip()

                if is_number(limite):
                    limite = float(limite)
                    limiteFalso = True
                    continue

        pessoa[nome] = {
            'nome': nome,
            'cpf': cpf,
            'idade': idade,
            'endereco': endereco,
            'limite': limite
        }

    elif opcao == 2:
        print("1 - Endereço")
        print("2 - Limite")
        print("3 - Tudo")
        print("0 - Cancelar")
        alteracao = input("Digite a opção que deseja alterar: ").strip()

        if is_int(alteracao):
            alteracao = int(alteracao)

            if alteracao >= 0 and alteracao <= 3:
                alteracaoCerta = True
            else:
                alteracaoCerta = False

                while not alteracaoCerta:
                    alteracao = input("Você digitou uma opção inválida, tente novamente: ").strip()

                    if is_int(alteracao):
                        alteracao = int(alteracao)

                        if alteracao >= 0 and alteracao <= 3:
                            alteracaoCerta = True
                            break
                        else:
                            alteracaoCerta = False
                    else:
                        alteracaoCerta = False
        else:
            alteracaoCerta = False

            while not alteracaoCerta:
                alteracao = input("Você digitou uma opção inválida, tente novamente: ").strip()

                if is_int(alteracao):
                    alteracao = int(alteracao)

                    if alteracao >= 0 and alteracao <= 3:
                        alteracaoCerta = True
                        break
                    else:
                        alteracaoCerta = False
                else:
                    alteracaoCerta = False

        if alteracao == 0:
            continue

        nome = input("Digite o nome de quem deseja alterar: ").strip()
        if nome in pessoa:
            nomeCerto = True
        else:
            nomeCerto = False

            while not nomeCerto:
                nome = input("O nome digitado não existe, tente novamente: ").strip()

                if nome in pessoa:
                    nomeCerto = True

        if alteracao == 1:
            pessoa[nome]['endereco'] = input("Digite o novo endereço: ").strip()
        elif alteracao == 2:
            limite = input("Digite o novo limite: ").strip()
            if is_number(limite):
                limite = float(limite)
            else:
                limiteFalso = False

                while not limiteFalso:
                    limite = input("Digite o limite apenas com números: ").strip()

                    if is_number(limite):
                        limite = float(limite)
                        limiteFalso = True
                        continue
            pessoa[nome]['limite'] = limite
        elif alteracao == 3:
            pessoa[nome]['endereco'] = input("Digite o novo endereço: ").strip()
            limite = input("Digite o novo limite: ").strip()
            if is_number(limite):
                limite = float(limite)
            else:
                limiteFalso = False

                while not limiteFalso:
                    limite = input("Digite o limite apenas com números: ").strip()

                    if is_number(limite):
                        limite = float(limite)
                        limiteFalso = True
                        continue
            pessoa[nome]['limite'] = limite
        else:
            continue
    elif opcao == 3:
        print(pessoa)
    elif opcao == 4:
        nome = input("Digite o nome de quem deseja alterar: ").strip()
        if nome in pessoa:
            nomeCerto = True
        else:
            nomeCerto = False

            while not nomeCerto:
                nome = input("O nome digitado não existe, tente novamente: ").strip()

                if nome in pessoa:
                    nomeCerto = True

        del pessoa[nome]

    else:
        break

continuar = False

lista = []
for i in pessoa:
    limite = pessoa[i]['limite']

    if limite > 1000:
        lista.append(i)

print(f"A lista de pessoas com mais de R$1.000,00 em limite são: {lista}")
