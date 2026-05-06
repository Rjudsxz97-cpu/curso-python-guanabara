'''Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas 
e o preço total.'''
#ENTRADA DE DADOS
area = float(input('tamanho da area(m²): '))
#PROCESSAMENTO
litros = area/3
latas = litros/18
preco = latas * 80
#saida de dados
print(f'litros:{litros:.2f}\n'
      f'latas: {latas:.2f}\n'
      f'preço total: R$ {preco:.2f}')

