"""
DEQ -> lista de alta perfomace
"""

from collections import deque

deq = deque('geek')

print(deq)

#ADICIONANDO NO COMEÇO
deq.appendleft('a')

print(deq)

#REMOVENDO DO COMEÇO
deq.popleft()

print(deq)