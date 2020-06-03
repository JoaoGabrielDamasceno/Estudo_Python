"""
seek() -> é usado para movimentar o cursor dentro do arquivo
"""


arquivo = open('texto_exemplo.txt')

print(arquivo.read())
arquivo.seek(0)

ret = arquivo.read()
ret = ret.split('\n')
print(ret)

#FECHAR O ARQUIVO
arquivo.close()


