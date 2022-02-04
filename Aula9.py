import shutil #Biblioteca para manipulacao de arquivos


#Abrir um arquivo que já existe ou criar um novo
#Sempre que um arquivo for aberto, ele deve ser fechado
arquivo = open('teste.txt','w') #'w' para nova escrita (sobrescreve o que ja existia)
arquivo.write('Minha primeira escrita')
arquivo.close()

arquivo = open('teste.txt','a') #'a' escreve a partir do que já existia no arquivo (append)
arquivo.write('\nSegunda linha')

#Escrever em arquivo (sobreescrever o que ja existia)
def escrever_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo,'w')
    arquivo.write(texto)
    arquivo.close()

#Atualizar arquivo (append)
def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

#Ler arquivo
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo)
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r') #'r' abrir para leitura
    aluno_nota = arquivo.read()

    lista_medias = []

    aluno_nota = aluno_nota.split('\n') #Separar string em lista (separa no caracter informado)
    for aluno in aluno_nota:
        notas = aluno.split(',')
        nome_aluno = notas[0]
        notas.pop(0)

        #Retorna uma lista de int (for dentro dos []), faz uma somatoria da lista de int
        #e divide pela quantidade de notas (len)
        media = lambda notas: sum([int(i) for i in notas])/len(notas)

        lista_medias.append({nome_aluno:media(notas)}) #Chama a função lambda criada dentro de 'media'

    return lista_medias

#Copiar arquivo
def copia_arquivo(nome_arquivo, destino):
    shutil.copy(nome_arquivo,destino)

#Mover arquivo
def move_arquivo(nome_arquivo, destino):
    shutil.move(nome_arquivo,destino)

if __name__ == '__main__':
    # aluno = '\nHenrique,8,8,10,10'
    # atualizar_arquivo('notas.txt',aluno)
    #atualizar_arquivo('Terceira linha\n')
    #ler_arquivo(diretorio)
    #medias = media_notas('notas.txt')
    #print(medias)
    #print('{nome} ficou com média: {media}'.format(nome=nome_aluno, media=media(notas)))
    copia_arquivo('notas.txt','C:/Users/Afonso E Juliana/Desktop/notas_novas.txt')
    move_arquivo('C:/Users/Afonso E Juliana/Desktop/notas_novas.txt','C:/Users/Afonso E Juliana/Downloads/')