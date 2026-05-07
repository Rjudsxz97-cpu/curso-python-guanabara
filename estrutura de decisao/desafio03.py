'''Faça um programa que verifique se uma 
letra digitada é "F" ou "M". 
Conforme a letra escrever:

    F - Feminino
    M - Masculino
    Sexo Inválido.
'''
#entrada de dados
sekisu = input('digite M para masculino ou F para feminino: \n').upper()
if sekisu == 'M':
    print('Masculino')
elif sekisu == 'F':
    print('Feminino')
else: print('invalido')
     