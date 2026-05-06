'''Faça um programa que peça o tamanho de um arquivo para download (em MB) 
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
aproximado de download do arquivo usando este link (em minutos).'''

#entrada de dados
tamanho = float(input('tamanho do arquivo(MB): '))
velocidade = float(input('velocidade do link(Mbps): '))
#processamento
tempo = (tamanho * 8) / velocidade
tempo_minutos = tempo / 60
#saida de dados
print(f'O tempo aproximado de download é de {tempo_minutos:.2f} minutos.')
