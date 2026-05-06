'''Faça um programa que peça 2 números inteiros 
e um número real. Calcule e mostre:

    O produto do dobro do primeiro com metade do segundo .
    A soma do triplo do primeiro com o terceiro.
    O terceiro elevado ao cubo.

'''
n1 = int(input('digite um numero inteiro aí: '))
n2 = int(input('digite outro numero inteiro seu safado: '))
n3 = float(input('digite um numero real: '))

print('o produto do dobro do primeiro com a metade do segundo é: {}'.format((n1*2)*(n2/2)))
print('a soma do triplo do primeiro com o terceiro é: {}'.format((n1*3)+n3))
print('o terceiro elevado ao cubo é: {}'.format(n3**3))
