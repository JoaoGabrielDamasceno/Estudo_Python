

#print("Qual seu nome?")
#nome = input()

# [1] Primeira maneira
#print("Seja Bem-Vinda %s" % nome)

#nome = input()
#print("Seja Bem-Vindo {0}". format(nome))

# [2] Segunda Maneira
#print(f"Seja Bem-Vindo {nome}")


# [3] Terceira Maneira
nome = input("Qual o seu nome?")

idade = input("Qual a sua idade?")

print(f"O {nome} nasceu em {2020 - int(idade)}")