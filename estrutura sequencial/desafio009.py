'''Faça um programa que peça a temperatura em 
graus Fahrenheit, transforme e mostre a 
temperatura em graus Celsius.'''

#entrada de dados
temp = float(input('qual a temperatura pai?' ))
#processamento
temp_celsius = (temp - 32) * 5 / 9
#saida de dados
print(f'a temperatura em graus celsius é {temp_celsius:.2f}ºC')