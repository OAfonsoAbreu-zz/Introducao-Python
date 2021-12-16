#Criação de conjunto
#Um conjunto não permite dados duplicados, ele os elimina
conjunto = {1, 2, 3, 4, 4, 2}
print(type(conjunto))
print(conjunto)

#Adicionar e remover itens em um conjunto
conjunto.add(5)
conjunto.discard(2)
print(conjunto)

#Uniao de conjuntos
#Une os dois conjuntos e elimina as duplicatas
conjunto2 = {2, 5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))

#Intersecção de conjuntos
#Retorna tudo em comum entre os conjuntos
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))

#Diferencao entre conjuntos
conjunto_diferenca1 = conjunto.difference(conjunto2)
print('Diferença do conjunto 1: {conjunto}'.format(conjunto=conjunto_diferenca1))
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença do conjunto 2: {conjunto}'.format(conjunto=conjunto_diferenca2))

#Diferença simétrica
#O que é diferente de ambos os lados
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

#Verificar subconjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é um subconjunto de B? {}'.format(conjunto_subset))

#Verificar superconjunto
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A? {}'.format(conjunto_superset))

#Converter lista para conjunto e remover duplicatas
lista = ['Cachorro', 'Gato', 'Leao', 'Cachorro', 'Leao']
conjunto_animais = set(lista)
print('Conjunto de animais: {}'.format(conjunto_animais))

#Converter conjunto para lista
lista_animais = list(conjunto_animais)
print('Lista de animais: {}'.format(lista_animais))