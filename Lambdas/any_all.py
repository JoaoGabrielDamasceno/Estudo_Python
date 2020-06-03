"""
ANY E ALL

All -> retorna se TODOS os elementos do iteravel são True ou o iteravel está vazio (vaio é false mas o all faz como se fosse true)
ANY -> retorna se ALGUM elemento do iteravel for True e se for vazio sera False
"""

print(all([0,1,2,3,4,5]))
print(all([1,2,3,4,5]))

nomes = ['Joao', 'Juliana', 'Joaquim']
print(all(nome[0].lower()== 'j' for nome in nomes))

print(any([0,1,2,3,4,5]))
print(any([0]))
