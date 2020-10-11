cpf = input('Digite seu CPF: ')
while True:
    if not len(cpf) == 11:
        print('Você não digitou apenas os 11 números.')
        cpf = input('Digite seu CPF: ')
    elif not cpf.isnumeric():
        print('Você não digitou APENAS números. Use somente números em seu CPF.')
        cpf = input('Digite seu CPF: ')
    else:
        break

cpf2 = list(cpf[:-2])
l0 = []
for n in range(10, 1, -1):
    p = (int(cpf2[10-n])*n)
    l0.append(p)
soma = sum(l0)
v = 11 - (soma % 11)
if v > 9:
    v2 = 0
else:
    v = str(v)
cpf2.append(v)

l1 = []
for n1 in range(11, 1, -1):
    p1 = (int(cpf2[11-n1])*n1)
    l1.append(p1)
soma1 = sum(l1)
v1 = 11 - (soma1 % 11)
if v1 > 9:
    v2 = 0
else:
    v1 = str(v1)
cpf2.append(v1)
cpf2 = ''.join(cpf2)

sequencia = cpf2 == str(cpf2[0]) * len(cpf)

if cpf == cpf2 and not sequencia:
    print('CPF Válido.')
else:
    print('CPF Inválido.')
"""
Resolução apresentada na correção
# cpf = 16899535009 
cpf = input('Digite seu CPF: ')
novo_cpf = cpf[:-2]
novo = 0
num = 10
for n in range(19):
    if n > 8:
        n -= 9

    novo += int(novo_cpf[n])*num

    num -= 1
    if num < 2:
        num = 11
        x = 11 - (novo % 11)

        if x > 9:
            x = 0
        novo = 0
        novo_cpf += str(x)

# Evita sequências. ex 111111111
if cpf == novo_cpf :
    print('CPF Válido')
else:
    print('CPF Inválido')"""