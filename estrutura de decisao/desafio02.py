'''Faça um programa que peça um 
valor e mostre na tela se o valor 
é positivo ou negativo.'''

a = int(input('===DIGITEE==UM==NÚMERO===:\n '))

if a < 0:
    print(f'Humm... esse nº é negativo :D')
elif a >= 0:
    print(f'Humm... esse nº é positivo :D')