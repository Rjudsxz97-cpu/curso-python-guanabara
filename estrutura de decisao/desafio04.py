'''Faça um programa que verifique se uma 
letra digitada é vogal ou consoante.'''

letra = input('digite uma letra: ').lower()
if len(letra) != 1 or not letra.isalpha():
    print('digite apenas uma letra!')

else:
    if letra in 'aeiou':
        print(f"A letra '{letra.upper()}' é uma vogal")
    else:
        print(f"A letra '{letra.upper()}' é uma consoante")