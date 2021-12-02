# #Uso do repeticao for
# #Uso do range para gerar uma sequencia de numeros baseado em zero
# #Pode iniciar em outro numero usando o renge(5, 100)
# #Neste caso inicia em 5 e vai até 99
# for x in range(101):
#     print(x)

# #Uso fo for com if
# a = int(input('Digite um numero e saiba se ele é primo: '))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     if resto == 0:
#         #div = div + 1
#         div += 1
# if(div == 2):
#     print('O numero {num} é primo!'
#           .format(num = a))
# else:
#     print('O numero {num} não é primo!'
#           .format(num = a))

# #Uso do for aninhado
# a = int(input('Entre com um numero: '))
# for numero in range(a + 1):
#     div = 0
#     for x in range(1, numero + 1):
#         resto = numero % x
#         if resto == 0:
#             #div = div + 1
#             div += 1
#     if(div == 2):
#         print('O numero {num} é primo!'
#               .format(num = numero))

#Uso do while
f = int(input('Nota do primeiro bimestre: '))
while f > 10 or f < 0:
    f = int(input('Voce digitou errado! Primeiro bimestre: '))
g = int(input('Nota do segundo bimestre: '))
while g > 10 or g < 0:
    g = int(input('Voce digitou errado! Segundo bimestre: '))
h = int(input('Nota do terceiro bimestre: '))
while h > 10 or h < 0:
    h = int(input('Voce digitou errado! Terceiro bimestre: '))
i = int(input('Nota do quarto bimestre: '))
while i > 10 or i < 0:
    i = int(input('Voce digitou errado! Quarto bimestre: '))

media = (f + g + h + i) / 4

if f <= 10 and g <= 10 and h <= 10 and i <= 10:
    print('Média: {med} '
      .format(med = media))
else:
    print('Foi informada alguma nota incorreta')