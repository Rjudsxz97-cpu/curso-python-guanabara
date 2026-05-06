'''Faça um programa para uma loja de tintas. O programa deverá pedir
o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 
6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
'''entrada de dados'''
area = float(input('tamanho da area(m²): '))
'''processamento'''
litros = area/6
latas = litros/18
galoes = litros/3.6
preco_latas = latas* 80
preco_galoes = galoes * 25
latas_mistura = int(litros/18)
galoes_mistura = int((litros - (latas_mistura*18))/3.6)
preco_mistura = (latas_mistura * 80) + (galoes_mistura * 25)
'''saida de dados'''
print(f'litros: {litros:.2f}')
print(f'latas: {latas:.2f}')
print(f'galões: {galoes:.2f}')
print(f'preço total em latas: R$ {preco_latas:.2f}')
print(f'preço total em galões: R$ {preco_galoes:.2f}')
print(f'preço total em mistura: R$ {preco_mistura:.2f}')