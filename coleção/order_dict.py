"""
Orderer Dict --> Dicionario em que a ordem de inserção dos elementos importa
"""

from collections import OrderedDict



d1 = {'a': 1, 'b': 5}
d2 = {'b': 5, 'a': 1}

if d1 == d2:
    print(True)
else:
    print(False)


dic1 = OrderedDict({'a': 1, 'b': 5})
dic2 = OrderedDict({'b': 5, 'a': 1})

if dic1 == dic2:
    print(True)
else:
    print(False)
