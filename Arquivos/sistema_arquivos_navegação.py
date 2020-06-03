"""
Para fazer a manipulação de arquivos no sistema operacional, precisa usar o módulo os

"""

import os

#Retorna o diretório atual
print(os.getcwd())

#Volta um diretório
os.chdir('..')

print(os.getcwd())

print(os.uname())