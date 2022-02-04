#Função retorna valor, Método não retorna

#Declarar método/função
if __name__ == '__main__':
    def soma(a, b):
        return a + b

    def subtracao(a, b):
        return a - b

    print('Soma: {}'.format(soma(1,2)))
    print('Soma: {}'.format(soma(3,4)))
    print('Subtração: {}'.format(subtracao(5,3)))

#Criar classe
class Calculadora:
    #Construtor
    def __init__(self, numero1, numero2):
        self.valor_a = numero1
        self.valor_b = numero2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    #Instanciar uma classe
    calculador = Calculadora(10, 5)
    print('Soma (Classe): {}'.format(calculador.soma()))
    print('Subtração (Classe): {}'.format(calculador.subtracao()))
    print('Multiplicação (Classe): {}'.format(calculador.multiplicacao()))
    print('Divisão (Classe): {}'.format(calculador.divisao()))


class Calculadora2:
    #Construtor vazio (Não precisa colocar quando for ser vazio)
    def __init__(self):
        pass #Para o construtor não ficar vazio

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

if __name__ == '__main__':
    calculador2 = Calculadora2() #Instanciar uma classe
    print('Soma (Classe2): {}'.format(calculador2.soma(1,2)))
    print('Subtração (Classe2): {}'.format(calculador2.subtracao(2,1)))
    print('Multiplicação (Classe2): {}'.format(calculador2.multiplicacao(3,6)))
    print('Divisão (Classe2): {}'.format(calculador2.divisao(12,6)))

class Televisao:

    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada: #O mesmo que self.ligada == True
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

if __name__ == '__main__':
    tv = Televisao()
    print('Status da TV: {}'.format(tv.ligada))
    tv.power()
    print('Status da TV: {}'.format(tv.ligada))
    tv.power()
    print('Status da TV: {}'.format(tv.ligada))
    tv.power()
    print('Status da TV: {}'.format(tv.ligada))
    print('Canal: {}'.format(tv.canal))
    tv.aumenta_canal()
    tv.aumenta_canal()
    print('Canal: {}'.format(tv.canal))
    tv.diminui_canal()
    tv.diminui_canal()
    tv.diminui_canal()
    print('Canal: {}'.format(tv.canal))
    tv.power()
    print('Status da TV: {}'.format(tv.ligada))
    tv.aumenta_canal()
    tv.aumenta_canal()
    print('Canal: {}'.format(tv.canal))