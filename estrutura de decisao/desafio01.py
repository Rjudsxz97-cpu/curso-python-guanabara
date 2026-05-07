'''Faça um programa que peça dois números e imprima o maior deles.'''
#ENTRADA DE DADOS
n1 = int(input('digite n1: '))
n2 = int(input('digite n2: '))
#processamento
if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n1 < n2:
    print(f'{n2} é maior que {n1}')