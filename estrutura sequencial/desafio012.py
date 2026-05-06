'''Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que
 faça a conversão para Megabytes, usando a seguinte fórmula:Gigabytes * 1024'''
#entrada de dados
gb = float(input('digite o valor em gigabytes: '))
#processamento
mb = gb*1024
#saida de dados
print(f'{gb} gigabytes é igual a {mb} megabytes')
