print('Gerador de CPF válido')

from random import randint
cpf = str(randint(100000000, 999999999))

cpf2 = list(cpf)
l0 = []
for n in range(10, 1, -1):
    p = (int(cpf2[10-n])*n)
    # print(p)
    l0.append(p)
soma = sum(l0)

v = 11 - (soma % 11)
if v > 9:
    v2 = 0
    print(v2)
else:
    # print(v)
    v = str(v)

cpf2.append(v)
# print(cpf2)
l1 = []
for n1 in range(11, 1, -1):
    p1 = (int(cpf2[11-n1])*n1)
    # print(p1)
    l1.append(p1)
    # print(l1)
soma1 = sum(l1)
v1 = 11 - (soma1 % 11)
if v1 > 9:
    v2 = 0
    print(v2)
else:
    # print(v1)
    v1 = str(v1)
cpf2.append(v1)
# print(cpf2)
cpf_str = ''.join(cpf2)

print('O número de CPF gerado é: ', end='')
print(cpf_str[:3], cpf_str[3:6], cpf_str[6:9], sep='.', end='-')
print(cpf_str[9:])