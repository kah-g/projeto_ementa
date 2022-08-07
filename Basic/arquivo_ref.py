#modulo que escreve a lista de refeicoes em um arquivo txt

def cria_modelo_refeicao ():
    #essa funcao cria um dicionario para uma refeicao com a keys necessarias
    nova_refeicao = {'Nome': ' ', 'Horario': ' ', 'Tipo': ' '}
    return nova_refeicao

def preenche_nome ():
    #antes de escrever uma nova refeicao, ela vai verificar se o nome existe
    print ("Entre com o nome da refeicao.")
    while True:
        nome = input ()
        if (nome.isalpha () == False):
            break
        else:
            print ("Erro: Nome invalido. Tente novamente")
            continue
    return nome


def cria_refeicao ():
    #essa funcao vai preencher os dados de uma refeicao seguindo o modelo pronto
    #para isso ela vai charm uma funcao que vai preencher cada key da refeicao
    refeicao = cria_modelo_refeicao ()
    refeicao['Nome'] = preenche_nome ()
    return refeicao

def escreve_arquivo ():
    #funcao que escreve a refeicao no arquivo
    print ("programa que escreve o arquivo com refeicoes")
    arquivo = open ('C:\\Users\\karin\\Documents\\Repositorios GitHub\\projeto_ementa\\Basic\\refeicoes.txt', 'a')
    refeicao = cria_refeicao ()
    for i, j in refeicao.items ():
        arquivo.write(i + ': ' + j + '\n')
    arquivo.close ()

escreve_arquivo ()
arquivo = open ('C:\\Users\\karin\\Documents\\Repositorios GitHub\\projeto_ementa\\Basic\\refeicoes.txt', 'r')
print (arquivo.read ())
arquivo.close ()