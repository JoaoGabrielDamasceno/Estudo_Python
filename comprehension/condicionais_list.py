"""
-Pode se adicionar condicionais nas list comprehensions
"""

numero = [1,2,3,4,5,6,7]

pares = [n for n in numero if not n % 2] #"NOT" POIS ESSE RESULTADO É IGUAL A 0 QUE SERIA CONSIDERADO FALSE, FAZENDO SALVAR OS NUMEROS IMPARES
print(pares)