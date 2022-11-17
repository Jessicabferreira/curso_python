nome = 'Jessica'
altura = 1.53
peso = 50
imc = peso / (altura * altura)

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilas e seu imc é '
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
