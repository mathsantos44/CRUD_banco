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

def verificarNumero(variavel, tipo, min, max):
    if is_number(variavel):
        variavel = tipo(variavel)

        if variavel >= min and variavel <= max:
            digCerto = True
        else:
            digCerto = False
    else:
        digCerto = False

    return digCerto

def verificarOpcao(tipo, min, max):
    variavel = input("Digite a opção desejada: ")

    digCerto = verificarNumero(variavel, tipo, min, max)

    while not digCerto:
        variavel = input("Opção inválida, por favor, tente novamente (Digite a opção em numerais): ")

        digCerto = verificarNumero(variavel, tipo, min, max)

    return variavel

def validarCPF(cpf):
    if is_number(cpf) and len(cpf) == 11:
        soma = 0

        cpf = [cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11]]


continuar = True

while continuar:
    print("1 - Incluir")
    print("2 - Alterar")
    print("3 - Exibir")
    print("4 - Excluir")
    print("0 - Sair")

    opcao = verificarOpcao(int, 0, 4)

    if opcao == 0:
        continuar = False
        break

    if opcao == 1:
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF (Somente números) : ")
        validarCPF(cpf)

