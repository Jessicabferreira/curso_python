"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o póximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Jessica'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)
    