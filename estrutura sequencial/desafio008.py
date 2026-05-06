'''Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
 e mostre o total do seu salário no referido mês.'''
#entrada de dados
ganho_hora = float(input('quanto voce ganha por hora? R$'))
horas_trabalhadas = float(input('quantas horas voce trabalhou no mes? '))
#processamento
salario_mes = ganho_hora * horas_trabalhadas
#saida de dados
print(f'o total do seu salario no referido mes é R${salario_mes:.2f}')

'''para que usar .2f? para mostrar 
o valor com 2 casas decimais, ou seja, 
 para mostrar o valor com centavos.'''

'''Sem o .2f, se o seu salário fosse 1500.0,
 o Python poderia exibir apenas 1500.0 ou 
 até algo como 1500.333333333. 
 Como estamos lidando com dinheiro (R$), 
 o padrão é sempre exibir dois dígitos centavos, 
 transformando o valor em 1500.00.Exemplo Prático:
 Sem formatar: R$1250.5
 Com :.2f: R$1250.50'''