#Instalar pacotes no Python
#Utilizar o pip no terminal
#Comandos: pip --version  --> Visualizar versão do pip
#pip lisl --> Visualizar o que já tem instalado
#Documentação do Python Requests: https://docs.python-requests.org/en/latest/
#pip install requests --> Instalar a biblioteca Python Requests
#pip freeze --> Ver o que acabou de ser instalado

import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{cep}/json/'.format(cep=cep))
    return response.json()

def retorna_dados_pockemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{pokemon}'.format(pokemon=pokemon))
    return response.json()

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    #Fazer um request em uma API
    response = requests.get('https://viacep.com.br/ws/01001000/json/')
    #Retorno de codigo de status da pagina
    print(response.status_code)
    #Retorno do texto da pagina
    print(response.text)
    #Ler retorno como um Json (e transformar em dicionario)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])

    print(retorna_dados_cep('04250090'))
    print(retorna_dados_pockemon('pikachu'))
    print(retorna_response('https://google.com'))