import random
# import sys
# import os
# def restart_program():
#     python = sys.executable
#     os.execl(python, python, * sys.argv)

# Criar um jogo para descobrir a palavra secreta
pr = '### Criar um jogo para descobrir a palavra secreta ###'
print(pr)
print()
digitados = []  # Lista vazia. Para salvar os caracteres digitados
chances = 3
print('Vamos jogar forca! Tente adivinhar a palavra secreta.\n'
      f'Atenção: você só pode errar {chances} vezes!\n')
lista = ['casa', 'cadeira', 'sofa', 'televisao', 'ventilador', 'travesseiro', 'tapete', 'sushi', 'rack']
lista1 = ['cama', 'ventilador', 'mesa', 'notebook', 'lençol', 'roupa', 'armario', 'livro', 'travesseiro']

secreto = ''
escolha = input('Você quer jogar forca com objetos da sala ou do quarto?\n'
                'Digite 1 para sala ou 2 para quarto: ')
while escolha != '1' and escolha != '2':
    print('ERRO! Escolha 1 para sala ou 2 para quarto!')
    escolha = input('Digite 1 ou 2: ')
else:
    if escolha == '1':
        numero = random.randrange(len(lista))
        secreto = lista[numero]
    elif escolha == '2':
        numero = random.randrange(len(lista1))
        secreto = lista[numero]
# import random
# numero = random.randrange(len(lista))
# print(numero)
# print(secreto)
# for letra in secreto:
#     print(letra)
# secreto = 'PERFUME'
# digitados = []  # Lista vazia. Para salvar os caracteres digitados
# chances = 3
# print('Vamos jogar forca! Tente adivinhar a palavra secreta.\n'
#           f'Atenção: você só pode errar {chances} vezes!\n')
print(f'A palavra é: {"*" * len(secreto)}. {len(secreto)} letras.\n')
while True:  # Jogo tipo forca
    if chances < 1:
        print('Você perdeu!\n'
              f'A palavra correta é {secreto}.')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1 or letra == '':  # Precisa checar a quantidade de caracteres digitado e se vazio
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    if letra in digitados:
        print('Você já digitou essa letra!\n')
        continue

    digitados.append(letra)

    if letra not in secreto:
        chances -= 1

    if letra in secreto:  # Checar se a letra faz parte do string criado
        print(f'UHHULLLL! A letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Pooxaa! A letra "{letra}" NÃO EXISTE na palavra secreta.')
        # digitados.pop()  # para retirar último elemento digitado
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitados:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print()
        print(f'Que legal! Você ganhou! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'{secreto_temporario.upper()}')
    # if letra not in secreto:
    #     chances -= 1
    print(f'Você tem {chances} chances.')
    print()
print()
# para reiniciar o módulo. Apantemente precisa de uma função emcima. E chamá-la.
# nova = input('Você quer jogar novamente? Digite (s)im ou (n)ão? ')
# while True:
#     if nova != 's' and nova != 'n':
#         print('ERRO! Você deve digitar s ou n.\n')
#         nova = input('Digite s para sim ou n para não: ')
#     else:
#         if nova == 's':
#             ...
#             # restart_program()
#         elif nova == 'n':
#             print('Volte sempre!')
#             break

        # print('Até mais!')
        # break


# para contar quantidade de elementos em lista
# qtd_lista = len(lista)
# print(qtd_lista)
