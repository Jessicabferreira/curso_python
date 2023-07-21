""" 
 Parte 3
Listas em Python
Tipo list - Mútavel
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, Adiciona um item ao final
    insert, Adiciona um item ni índice escolhido
    pop, Remove do final ou do índice escolhido
    del, Apaga um índice
    clear, Limpa a lista
    extend, Estende a lista
    + concatena listas
Create, Read,  Update,    Delete
Criar,  ler ,  alterar,   apagar = lista[i] (CRUD)
"""
#........0....1...2...3
lista = [10, 20, 30, 40]
lista.append('Jessica')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lista[4])
