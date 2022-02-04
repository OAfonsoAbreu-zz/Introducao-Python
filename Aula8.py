#Cada arquivo .py é um módulo em Python
#Ex: no Pythom console digite:
#import Aula7, e ele executa tudo do módulo Aula7.py
#Outra forma é importar exatamente o que precisa de dentro do módulo
#Exemplo: from Aula7 import Televisao

from Aula7 import Televisao
from Aula7 import Calculadora2
#Importar multiplos métodos ou classes de um módulo
from ContadorDeLetras import contador_letras, teste

if __name__ == '__main__':
    #Instanciar classe de outro m'odulo e usar seus métodos
    tv = Televisao()
    print(tv.ligada)

    calc = Calculadora2()
    print(calc.soma(3,6))

    #Usar método/função de outro módulo
    lista = ['Gato', 'Cachorro', 'Rato']
    print(contador_letras(lista))
    print(teste())