import random

#Aqui ficam as funções de cada dado

def rolard2(rolagens):
    lista = []
    for i in range(0,rolagens):
        d2 = random.randint(1,2)
        print(d2)
        lista.append(d2)
    s = sum(lista)
    print('{} Resultado: {}'.format(lista,s))


def rolard4(rolagens):
    lista = []
    for i in range(0, rolagens):
        d4 = random.randint(1, 4)
        print(d4)
        lista.append(d4)
    s = sum(lista)
    print('{} Resultado: {}'.format(lista,s))

def rolard6(rolagens):
    lista = []
    for i in range(0, rolagens):
        d6 = random.randint(1, 6)
        print(d6)
        lista.append(d6)
    s = sum(lista)
    print('{} Resultado: {}'.format(lista, s))

def rolard8(rolagens):
    lista = []
    for i in range(0, rolagens):
        d8 = random.randint(1, 8)
        print(d8)
        lista.append(d8)
    s = sum(lista)
    print('{} Resultado: {}'.format(lista, s))

def rolard10(rolagens):
    lista = []
    for i in range(0, rolagens):
        d10 = random.randint(1, 10)
        print(d10)
        lista.append(d10)
    s = sum(lista)
    print('{} Resultado: {}'.format(lista, s))

def rolard12(rolagens):
    lista = []
    for i in range(0, rolagens):
        d12 = random.randint(1, 12)
        print(d12)
        lista.append(d12)
    s = sum(lista)
    print('{} Resultado: {}'.format(lista, s))

def rolard20(rolagens):
    lista = []
    for i in range(0, rolagens):
        d20 = random.randint(1, 20)
        print(d20)
        lista.append(d20)
    s = sum(lista)
    print('{} Resultado: {}'.format(lista, s))

def rolard100(rolagens):
    lista = []
    for i in range(0, rolagens):
        d100 = random.randint(1, 100)
        print(d100)
        lista.append(d100)
    s = sum(lista)
    print('{} Resultado: {}'.format(lista, s))

#Aqui é o menu
    
def imprimir_menu():
    print('Seja bem vindo ao Dice Roll!')
    print('d2 - Dado de dois lados ')
    print('d4 - Dado de quatro lados ')
    print('d6 - Dado de seis lados ')
    print('d8 - Dado de oito lados ')
    print('d10 - Dado de dez lados ')
    print('d12 - Dado de doze lados ')
    print('d20 - Dado de vinte lados ')
    print('d100 - Dado de cem lados ')

imprimir_menu()

while True:

    choice = str(input('Diga o dado desejado: '))

    if choice == 'd2':
        try:
            rolagens = int(input('Diga quantas rolagens deseja fazer: '))
            rolard2(rolagens)
        except Exception as e:
             print('Por favor, digite um número inteiro aqui da próxima vez.')
    elif choice == 'd4':
        try:
            rolagens = int(input('Diga quantas rolagens deseja fazer: '))
            rolard4(rolagens)
        except Exception as e:
            print('Por favor, digite um número inteiro aqui da próxima vez.')
    elif choice == 'd6':
        try:
            rolagens = int(input('Diga quantas rolagens deseja fazer: '))
            rolard6(rolagens)
        except Exception as e:
            print('Por favor, digite um número inteiro aqui da próxima vez.')
    elif choice == 'd8':
        try:
            rolagens = int(input('Diga quantas rolagens deseja fazer: '))
            rolard8(rolagens)
        except Exception as e:
            print('Por favor, digite um número inteiro aqui da próxima vez.')
    elif choice == 'd10':
        try:
            rolagens = int(input('Diga quantas rolagens deseja fazer: '))
            rolard10(rolagens)
        except Exception as e:
            print('Por favor, digite um número inteiro aqui da próxima vez.')
    elif choice == 'd12':
        try:
            rolagens = int(input('Diga quantas rolagens deseja fazer: '))
            rolard12(rolagens)
        except Exception as e:
            print('Por favor, digite um número inteiro aqui da próxima vez.')
    elif choice == 'd20':
        try:
            rolagens = int(input('Diga quantas rolagens deseja fazer: '))
            rolard20(rolagens)
        except Exception as e:
            print('Por favor, digite um número inteiro aqui da próxima vez.')
    elif choice == 'd100':
        try:
            rolagens = int(input('Diga quantas rolagens deseja fazer: '))
            rolard100(rolagens)
        except Exception as e:
            print('Por favor, digite um número inteiro aqui da próxima vez.')
    else:
        print('Dado inexistente, escolha um dado da lista')
