#Função anonima Lambda
#Sitaxe: nome_da_funcao = lambda parametro_entrada: retorno
#Utiliza lambda em coisas que se pode resolver em uma unica linha
contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['Gato','Cachorro','Rato']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(2, 5))
print(subtracao(5, 4))

#Criar dicionario de função lambda
calculadora = {
    'Soma': lambda a, b : a + b,
    'Sub': lambda a, b : a - b,
    'Mult': lambda a, b : a * b,
    'Div': lambda a, b : a / b
}
print(type(calculadora))

#Usando o dicionario de função lambda
soma = calculadora['Soma']
mult = calculadora['Mult']

print(soma(2,3))
print(mult(2,3))