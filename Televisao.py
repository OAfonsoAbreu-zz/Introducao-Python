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

print('Classe que está chamando é: {}'.format(__name__))

#Somente executa esse trecho se quem estiver chamando for a propria classe
#Não irá chamar se quem executar for uma classe externa
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