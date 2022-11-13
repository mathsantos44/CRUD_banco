"""
cpf = input("Digite o CPF: ")

posicao = 0
cont = 10
soma = 0

while posicao < 9:
    soma += int(cpf[posicao]) * cont
    cont -= 1
    posicao += 1

verificador1 = (soma * 10) % 11
print(verificador1)

posicao = 0
cont = 11
soma = 0
while posicao < 10:
    soma += int(cpf[posicao]) * cont
    cont -= 1
    posicao += 1

verificador2 = (soma * 10) % 11
print(verificador2)

if verificador1 == int(cpf[9]) and verificador2 == int(cpf[10]):
    for i in range(0, 11):
        if cpf[i] != cpf[i - 1]:
            digCerto = True
            break
        else:
            digCerto = False
else:
    digCerto = False

while digCerto == False:
    cpf = input("CPF inválido, tente novamente: ")

    posicao = 0
    cont = 10
    soma = 0

    while posicao < 9:
        soma += int(cpf[posicao]) * cont
        cont -= 1
        posicao += 1

    verificador1 = (soma * 10) % 11
    print(verificador1)

    posicao = 0
    cont = 11
    soma = 0
    while posicao < 10:
        soma += int(cpf[posicao]) * cont
        cont -= 1
        posicao += 1

    verificador2 = (soma * 10) % 11
    print(verificador2)

    if verificador1 == int(cpf[9]) and verificador2 == int(cpf[10]):
        for i in range(0, 11):
            if cpf[i] != cpf[i - 1]:
                digCerto = True
                break
            else:
                digCerto = False

print(cpf)
"""
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

def verificar(cpf, nummax):
    posicao = 0
    cont = nummax + 1
    soma = 0

    while posicao < nummax:
        soma += int(cpf[posicao]) * cont
        cont -= 1
        posicao += 1
    print(soma)
    return (soma * 10) % 11

def verificarIguais(cpf):
    for i in range(0, 11):
        if cpf[i] != cpf[i - 1]:
            return True
    return False

def verificarCPF(cpf):
    if is_number(cpf) and len(cpf) == 11:
        verificador1 = verificar(cpf, 9)
        print(verificador1)
        verificador2 = verificar(cpf, 10)
        print(verificador2)

        if verificador1 == int(cpf[9]) and verificador2 == int(cpf[10]) and verificarIguais(cpf):
            digCerto = True
        else:
            digCerto = False
    else:
        digCerto = False

    return digCerto

cpf = input("Digite o CPF: ")

digCerto = verificarCPF(cpf)

while not digCerto:
    cpf = input("CPF digitado inválido, por favor, tente novamente: ")

    digCerto = verificarCPF(cpf)

cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
print(cpf)


