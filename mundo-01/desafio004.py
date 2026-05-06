'''
DESAFIO 004: Dissecando uma Variável
Faça um programa que leia algo pelo teclado e mostre na tela o seu 
tipo primitivo e todas as informações possíveis sobre ele.
'''

# Lendo a entrada do teclado
algo = input('Digite algo: ')

# Mostrando o tipo primitivo (No input, ele sempre vem como 'str')
print(f'O tipo primitivo desse valor é: {type(algo)}')

# Usando os métodos 'is' para investigar a variável
print(f'Só tem espaços? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético (letras)? {algo.isalpha()}')
print(f'É alfanumérico (letras ou números)? {algo.isalnum()}')
print(f'Está em maiúsculas? {algo.isupper()}')
print(f'Está em minúsculas? {algo.islower()}')
print(f'Está capitalizada (Maiúscula e minúscula)? {algo.istitle()}')