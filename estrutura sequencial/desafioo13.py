'''Tendo como dados de entrada um arquivo em Gigabytes, 
construa um algoritmo que faça a conversão para Megabytes 
e Kilobytes, usando as seguintes fórmulas:

    Para Megabytes: Gigabytes * 1024
    Para Kilobytes: Gigabytes * 1024 * 1024
Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes'''
# Entrada de dados
arquivo_gb = float(input('digite o tamanho do arquivo em gigabytes: '))
# Processamento
arquivo_mb = arquivo_gb * 1024
arquivo_kb = arquivo_gb * 1024 * 1024
#saida de dados 
print(f'o tamanho do arquivo em megabytes é:{arquivo_mb} MB')
print(f'o tamanho do arquivo em kilobytes é:{arquivo_kb} KB')
