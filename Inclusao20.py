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

    return int(variavel)

def validarCPF(cpf):
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
        if is_number(cpf) and len(cpf) == 11:
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


continuar = True

while continuar:
    print("1 - Incluir")
    print("2 - Alterar")
    print("3 - Exibir")
    print("4 - Excluir")
    print("0 - Sair")

    opcao = verificarOpcao(int, 0, 4)

    if opcao == 1:
        nome = input("Digite o nome do cliente: ").strip()
        cpf = input("Digite o CPF: ").strip()
        cpf = validarCPF(cpf)