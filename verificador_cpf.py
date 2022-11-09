cpf = "52998224725"

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

cpf = [cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11]]
