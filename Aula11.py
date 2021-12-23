#Tratamento de exceção
lista = [1 , 10]
try:
    arquivo = open('teste2.txt', 'r')
    divisao = 10 / 1
    numero = lista[1]
#Tratamento de erro conhecido
#Hierarquia de exceptions em: https://docs.python.org/3/library/exceptions.html
except ZeroDivisionError:
    print('Não é possível realizar divisão por zero.')
except ArithmeticError: #Mais genérico do que ZeroDivisionError
    print('Ocorreu um erro ao realizar uma  operação aritmética.')
except IndexError:
    print('Erro ao tentar acessar um indice da lista.')

#Tratamento de erro generico
# except:
#     print('Ocorreu um erro desconhecido.')

#BaseException é a classe-mãe de todos os exceptions
# except BaseException as ex:
#     print('Erro desconhecido. Erro: {}'.format(ex))

#Exception recebe quase todos as Exceptions
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))

#Executar quando não ocorrer nenhum erro
else:
    print('Não ocorreu nenhum erro.')

#Sempre executa, com erro ou não
finally:
    print('Sempre executa')
    arquivo.close()