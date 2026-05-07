p1 = float(input('Preço do Produto 1: '))
p2 = float(input('Preço do Produto 2: '))
p3 = float(input('Preço do Produto 3: '))

# Decisão baseada apenas no mais barato
if p1 <= p2 and p1 <= p3:
    print(f'Você deve comprar o Produto 1, pois custa R$ {p1:.2f}')
elif p2 <= p1 and p2 <= p3:
    print(f'Você deve comprar o Produto 2, pois custa R$ {p2:.2f}')
else:
    print(f'Você deve comprar o Produto 3, pois custa R$ {p3:.2f}')