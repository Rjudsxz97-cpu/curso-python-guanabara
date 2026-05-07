n1 = int(input('n1: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))

# Caso o n1 seja o maior
if n1 >= n2 and n1 >= n3:
    maior = n1
    if n2 <= n3:
        menor = n2
    else:
        menor = n3

# Caso o n2 seja o maior
elif n2 >= n1 and n2 >= n3:
    maior = n2
    if n1 <= n3:
        menor = n1
    else:
        menor = n3

# Caso o n3 seja o maior (é a única opção que sobra)
else:
    maior = n3
    if n1 <= n2:
        menor = n1
    else:
        menor = n2

print(f'O maior é {maior} e o menor é {menor}')