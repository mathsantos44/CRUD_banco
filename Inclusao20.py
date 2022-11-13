import re

def main():
    continuar = True

    pessoa = {}

    while continuar:
        print("1 - Incluir")
        print("2 - Alterar")
        print("3 - Exibir")
        print("4 - Excluir")
        print("0 - Sair")

        opcao = verificarOpcao(0, 4)

        if opcao == 0:
            continuar = False
            break

        elif opcao == 1:
            nome = input("Digite o nome do cliente: ").strip()
            cpf = validarCPF()
            idade = input("Digite a idade: ")
            idade = validarNumero(idade, int, "Idade inválida, tente novamente: ")
            endereco = input("Digite o endereço: ")
            limite = input("Digite o limite: ")
            limite = validarNumero(limite, float, "Limite inválido, tente novamente: ")

            pessoa[nome] = {
                'nome': nome,
                'cpf': cpf,
                'idade': idade,
                'endereco': endereco,
                'limite': limite
            }
            print("Novo cliente adicionado: ", pessoa[nome], sep="")
            print()

        elif opcao == 2:
            if len(pessoa.keys()) > 0:
                print("Digite 0 caso queira sair")
                nome = input("Digite o nome do cliente que quer alterar: ")
                if nome == "0":
                    continue
                elif nome in pessoa.keys():
                    print("1 - Idade")
                    print("2 - Endereço")
                    print("3 - Limite")
                    print("4 - Todos os campos")
                    print("0 - Sair")
                    alteracao = verificarOpcao(0, 4)

                    if alteracao == 1:
                        idade = input("Digite a nova idade: ")
                        idade = validarNumero(idade, int, "Idade inválida, tente novamente: ")
                        pessoa[nome]['idade'] = idade

                        print("Cliente alterado: ", pessoa[nome], sep="")
                        print()
                    elif alteracao == 2:
                        endereco = input("Digite o novo endereço: ")
                        pessoa[nome]['endereco'] = endereco

                        print("Cliente alterado: ", pessoa[nome], sep="")
                        print()
                    elif alteracao == 3:
                        limite = input("Digite o novo limite: ")
                        limite  = validarNumero(limite, float, "Limite inválido, tente novamente: ")
                        pessoa[nome]['limite'] = limite
                        print("Cliente alterado: ", pessoa[nome], sep="")
                        print()
                    elif alteracao == 4:
                        idade = input("Digite a nova idade: ")
                        idade = validarNumero(idade, int, "Idade inválida, tente novamente: ")
                        pessoa[nome]['idade'] = idade
                        endereco = input("Digite o novo endereço: ")
                        pessoa[nome]['endereco'] = endereco
                        limite = input("Digite o novo limite: ")
                        limite = validarNumero(limite, float, "Limite inválido, tente novamente: ")
                        pessoa[nome]['limite'] = limite

                        print("Cliente alterado: ", pessoa[nome], sep="")
                        print()
                else:
                    print("Cliente inexitente, tente novamente!")
            else:
                print("Você precisa fazer primeiro uma inclusào para conseguir alterar!")
        elif opcao == 3:
            print(pessoa)
        elif opcao == 4:
            if len(pessoa.keys()) > 0:
                print("Digite 0 caso queira cancelar")
                deletar = input("Digite o nome do cliente que deseja excluir: ")

                if deletar == "0":
                    continue
                elif deletar in pessoa.keys():
                    del pessoa[deletar]
                else:
                    print("Cliente não existente, tente novamente: ")
            else:
                print("Para excluir um cliente, você precisa primeiramente incluir alguém na lista")

    lista = []
    for i in pessoa:
        limite = pessoa[i]['limite']

        if limite > 1000:
            lista.append(i)

    print(f"A lista de pessaos com mais de R$1.000,00 em limite são: {lista}")


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



def verificarOpcao(min, max):
    def verificarNumero(variavel, min, max):
        if is_number(variavel):
            variavel = int(variavel)

            if variavel >= min and variavel <= max:
                digCerto = True
            else:
                digCerto = False
        else:
            digCerto = False

        return digCerto

    variavel = input("Digite a opção desejada: ")

    digCerto = verificarNumero(variavel, min, max)

    while not digCerto:
        variavel = input("Opção inválida, por favor, tente novamente (Digite a opção em numerais): ")

        digCerto = verificarNumero(variavel, min, max)

    return int(variavel)

def validarCPF():
    cpf = input("Digite o CPF (Somente números): ").strip()

    def verificar(cpf, nummax):
        posicao = 0
        cont = nummax + 1
        soma = 0

        while posicao < nummax:
            soma += int(cpf[posicao]) * cont
            cont -= 1
            posicao += 1
        return (soma * 10) % 11

    def verificarIguais(cpf):
        for i in range(0, 11):
            if cpf[i] != cpf[i - 1]:
                return True
        return False

    def verificarCPF(cpf):
        if is_int(cpf) and len(cpf) == 11:
            verificador1 = verificar(cpf, 9)
            verificador2 = verificar(cpf, 10)

            if verificador1 == int(cpf[9]) and verificador2 == int(cpf[10]) and verificarIguais(cpf):
                digCerto = True
            else:
                digCerto = False
        else:
            digCerto = False

        return digCerto

    digCerto = verificarCPF(cpf)

    while not digCerto:
        cpf = input("CPF digitado inválido, por favor, tente novamente: ")

        digCerto = verificarCPF(cpf)

    cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])

    return cpf

def validarNumero(variavel, tipo, msg):
    def verificarTipo(variavel, tipo):
        if tipo == int:
            variavel = float(variavel)
            variavel = variavel // 1
            variavel = int(variavel)
        else:
            variavel = float(variavel)

    def verificarNumero(variavel, tipo):
        numeroCerto = True
        if is_number(variavel):
            verificarTipo(variavel, tipo)
            numeroCerto = True
        else:
            numeroCerto = False

        return numeroCerto

    numeroCerto = verificarNumero(variavel, tipo)
    while not numeroCerto:
        variavel = input(msg)
        numeroCerto = verificarNumero(variavel, tipo)

    return variavel

if __name__ == '__main__':
    main()