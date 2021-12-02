# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# #Uso so if/elif/else
# #Uso do and
# #blocos são organizados com identações
# if a > b and a > c:
#     print('O maior numero é: {maior}'
#           .format(maior = a))
# elif b > a and b > c:
#     print('O maior numero é: {maior}'
#           .format(maior = b))
# else:
#     print('O maior numero é: {maior}'
#           .format(maior = c))
# print('Fora dos ifs')

# #Uso do or e not
# d = int(input('Primeio valor: '))
# e = int(input('Segundo valor: '))
#
# resto_d = d % 2
# resto_e = e % 2
#
# if resto_d == 0 or not resto_e > 0:
#     print('Tem um numero par')
# else:
#     print('Nao em um numero par')

#validação de entrada com if
f = int(input('Nota do primeiro bimestre: '))
if f > 10:
    f = int(input('Voce digitou errado! Primeiro bimestre: '))
g = int(input('Nota do segundo bimestre: '))
if g > 10:
    g = int(input('Voce digitou errado! Segundo bimestre: '))
h = int(input('Nota do terceiro bimestre: '))
if h > 10:
    h = int(input('Voce digitou errado! Terceiro bimestre: '))
i = int(input('Nota do quarto bimestre: '))
if i > 10:
    i = int(input('Voce digitou errado! Quarto bimestre: '))

media = (f + g + h + i) / 4

if f <= 10 and g <= 10 and h <= 10 and i <= 10:
    print('Média: {med} '
      .format(med = media))
else:
    print('Foi informada alguma nota incorreta')