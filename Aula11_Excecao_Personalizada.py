#Para personalizar exception, precisa de uma classe vazia que herde de Exception
#E uma classe que Herda dessa classe vazia
class Error(Exception): #Herda de Exception
    pass

class InputError(Error): #Herda de Error
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: ')) #input() leitura de valor
        print(x)
        if x > 10:
            #raise força um erro
            raise InputError('Nota não pode ser maior que 10.')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0.')
        break #Força saida do looping
    except ValueError:
        print('Valor inválid. Deve-se sigitar apenas números.')
    except InputError as ex:
        print(ex)
