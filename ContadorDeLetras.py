def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        qtd_letras = len(x)
        contador.append(qtd_letras)

    return  contador

def teste():
    return 'Teste'

if __name__ == '__main__':
    lista = ['Cachorro', 'Gato']
    print(contador_letras(lista))