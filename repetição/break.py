#Exemplo 1
for i in range(1,10):
    if i == 6:
        break
    else:
        print(i)
print('Sai do loop')

while True:
    comando = input('Digite sair para acabar o loop: ')
    if comando == 'sair':
        break