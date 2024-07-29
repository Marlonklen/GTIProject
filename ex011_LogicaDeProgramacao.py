def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def cria_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'wt')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nome_arquivo))


def existe_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def listar_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

def cadastrar_jogo(nome_arquivo, nome_jogo, nome_video_game):
    try:
        a = open(nome_arquivo, 'at')
    except:
        print('Erro ao abrir arquivo!')
    else:
        a.write('{};{}\n'.format(nome_jogo,nome_video_game))
    finally:
        a.close()

#Programa Principal
arquivo = 'games.txt'
if existe_arquivo(arquivo):
    print('Arquivo localizado no computador.')
else:
    print('Arquivo inexistente!')
    cria_arquivo(arquivo)
while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - sair')

    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if op == 1:
        print('Opção cadastrae intem selecionada...\n')
        nome_jogo = input('Nome do jogo: ')
        nome_video_game = input('Nome video game: ')
        cadastrar_jogo(arquivo, nome_jogo, nome_video_game)
    elif op == 2:
        print('Opção listar selecionada...\n')
        listar_arquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa!')
        break




