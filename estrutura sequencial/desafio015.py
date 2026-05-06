'''Faça um programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% 
 para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido.'''
#ENTRADA DE DADOS
hora = float(input('valor da hora trabalhada: R$ '))
horas_mes = float(input('horas mês: '))
#PROCESSAMENTO
bruto = hora * horas_mes
ir = bruto * 0.11
inss = bruto * 0.08
sdc = bruto * 0.05
descontos = ir + inss + sdc 
liquido = bruto - descontos 
#SAIDA DE DADOS
print(f'+ salário bruto: R$ {bruto:.2f}\n'
      f'- IR (11%): R$ {ir:.2f}\n'
      f'- INSS (8%): R$ {inss:.2f}\n'
      f'- sindicato (5%): R$ {sdc:.2f}\n'
      f'= liquido: R$ {liquido:.2f}')
