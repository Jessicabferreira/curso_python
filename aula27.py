"""
Formatação de strings
 012345678
 Olá mundo
-987654321
Fatiamnto [i:f:p] [::]
obs.: a função len retorna a qtd
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:])
print(variavel[:5])
print(variavel[3])  # o espaço é um caracter válido
print(variavel[-8:-2])
print(len(variavel))
print(variavel[0:9:2]) # passo ele pula o caracter
print(variavel[::-1]) # vai inverter a string