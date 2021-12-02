a_old = 10
b_old = 5

#Interação com o usuário
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

#Operadores aritméticos
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

#Verificando Tipo e fazendo conversão
print(type(soma))
print(soma)

print('soma: ' + str(soma))
soma = str(soma) #Converte para string
print(type(soma))

#comentario
print(subtracao)
print(multiplicacao)

print(type(divisao))
print(int(divisao)) #Converte para int
print(divisao)

print(resto)

#Trabalhando com string
#Converte para string e coloca dentro das chaves na ordem do format
print('Soma: {} - Subtração: {} - Multiplicação: {} - Divisão: {} - Resto: {}'
      .format(soma,
              subtracao,
              multiplicacao,
              divisao,
              resto))

#Converte para string e coloca dentro das chaves conforme cada alias, não necessariamente na ordem
print('\tSoma: {soma} '
      '\n\r\tSubtração: {sub} '
      '\n\r\tMultiplicação: {mult} '
      '\n\r\tDivisão: {div} '
      '\n\r\tResto: {rest}'
      .format(soma = soma,
              mult = multiplicacao,
              sub = subtracao,
              div = divisao,
              rest = resto))

#Guardando a string em uma variavel
resultado = ('\tSoma: {soma} '
      '\n\r\tSubtração: {sub} '
      '\n\r\tMultiplicação: {mult} '
      '\n\r\tDivisão: {div} '
      '\n\r\tResto: {rest}'
      .format(soma = soma,
              mult = multiplicacao,
              sub = subtracao,
              div = divisao,
              rest = resto))

print(resultado)

#string to int
# x = '1'
#
# soma2 = int(x) + 6
# print(soma2)