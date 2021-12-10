lista_numeros = [1, 3 ,5, 7]
lista_animais = ['Elefante','Cachorro', 'Zebra', 'Gato', 'Elefante', 'Abelha']

print(lista_numeros)
print(lista_animais[1]) #Indices baseados em zero

for x in lista_animais: #Similar ao foreach
    print(x)

soma = 0
for x in lista_numeros:
    print(x)
    soma += x
print('Soma: {soma}'.format(soma = soma))
print('Soma (com sum): {soma}'.format(soma = sum(lista_numeros)))
print('Maior valor: {max}'.format(max=max(lista_numeros)))
print('Menor valor: {min}'.format(min=min(lista_numeros)))

print('Ultima string (ordem alfabetica): {max}'.format(max=max(lista_animais)))
print('Primeira string (ordem alfabetica): {min}'.format(min=min(lista_animais)))

#Verificar se existe um elemento na lista
animal = 'Lobo'
if animal in lista_animais:
    print('Existe esse animal na lista')
else:
    print('Não existe esse animal na lista')
    #Adiciona um item na lista
    lista_animais.append(animal)
    print(lista_animais)

#Remove o ultimo da lista
lista_animais.pop()
print(lista_animais)

#Remove o  item no indice informado
lista_animais.pop(2)
print(lista_animais)

#Remove o primeiro item com o nome informado
lista_animais.remove('Elefante')
print(lista_animais)

#Multiplicação de lista
nova_lista = lista_animais * 3
print(nova_lista)

#Ordenar lista ordem crescente
lista_animais.sort()
lista_numeros.sort()
print(lista_animais)
print(lista_numeros)

#Ordenar lista ordem decrescente
lista_numeros.sort(reverse=1)
lista_animais.reverse()
print(lista_numeros)
print(lista_animais)

#Tupla (é imutável), não é possivel atribuir novo valor
tupla = (1, 10, 14, 12)
print(tupla[1])

#Contar itens da tupla ou lista
print(len(tupla))
print(len(lista_animais))

#Converter lista em Tupla
tupla_animais = tuple(lista_animais)
print(type(tupla_animais))
print(tupla_animais)

#Converter tupla em lista
lista_tupla = list(tupla)
print(type(lista_tupla))
lista_tupla[0] = 100
print(lista_tupla)