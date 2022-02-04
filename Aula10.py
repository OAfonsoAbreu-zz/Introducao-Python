#Importar módulos para manipulação de datas
from datetime import date, time, datetime, timedelta

def trabalahdo_com_date():
    #Recuperar dia atual
    data = date.today()
    print(data)
    print(type(data))
    #Formatar data para o padrão desejado
    #Diretivas do date em : https://docs.python.org/3/library/datetime.html
    data_atual_format = data.strftime('%d/%m/%Y')
    print(data_atual_format) # %d -> dia | %m -> mês | %Y -> ano (aaaa)
    print(type(data_atual_format))

def trabalhando_com_time():
    #Criar um horario
    horario = time(hour=15, minute= 10, second=46)
    print(horario)
    print(type(horario))
    horario_format = horario.strftime('%H : %M : %S')
    print(horario_format) # %H -> horas | %M -> minutos | %S -> segundos
    print(type(horario_format))

def trabalhando_com_datetime():
    #Recuperando data e hora atual
    data_atual = datetime.now()
    print(data_atual)
    print(type(data_atual))
    data_atual_format = data_atual.strftime('%d/%m/%Y -- %H:%M:%S')
    print(data_atual_format)
    print(type(data_atual_format))
    print(data_atual.strftime('%c'))
    #Usar dados separados
    print(data_atual.day)
    print(type(data_atual.day))
    print(data_atual.month)
    print(type(data_atual.month))
    print(data_atual.year)
    print(type(data_atual.year))
    print(data_atual.hour)
    print(type(data_atual.hour))
    print(data_atual.weekday())
    print(type(data_atual.weekday()))

    #Traduzir o weekday()
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo', 'Domingo')
    print(tupla[data_atual.weekday()])

    #Criar data
    data_criada = datetime(2013,12,23,23,33,30)
    print(data_criada)
    print(data_criada.strftime('%d/%m/%Y -- %H:%M:%S'))

    #Ler data de string
    data_string = '17/07/1996 01:43:59'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    print(type(data_convertida))
    print(tupla[data_convertida.weekday()])

    #Subtração e soma de data
    nova_data = data_convertida - timedelta(days=365, hours=1, minutes=3, seconds=15)
    print(nova_data)
    nova_data = data_convertida + timedelta(days=365, hours=1, minutes=3, seconds=15)
    print(nova_data)

if __name__ == '__main__':
    #trabalahdo_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()