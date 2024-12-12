from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de ler o conteudo do arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção Cadastrar uma nova pessoa.
        cabeçalho('\033[32mNOVO CADASTRO\033[m')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção sair do sistema.
        cabeçalho('Saindo do sistema... Volte sempre!')
        break
    else:
        cabeçalho('\t\033[30;41mERRO: Digite uma opção válida!\033[m')
    sleep(1.5)



