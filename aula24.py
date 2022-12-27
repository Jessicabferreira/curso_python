# Operadores in e not in
# 'in' estar entre /  'not in' não estar entre
# string são iteráveis
#  0 1 2 3 4 5 6
#  j e s s i c a
# -7-6-5-4-3-2-1

"""
nome = 'Jessica'
print(nome[2])
print(nome[-5])
print('Jess' in nome)
print('z' in nome)
print(10 * '-')
print('Jess' not in nome)
print('z' not in nome)
"""

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
    