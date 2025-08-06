# Receba uma lista de palavras e ordene-a em ordem alfabética.

# 1. Criar um array vazio

minha_lista = []

# 2. Definir uma quantidade de palavras (5 palavras, por exemplo)

# 3. Criar a lógica para receber as palavras e adicionar no array

for i in range(1,6):
    palavra = input()
    print("Palavra adicionada")
    minha_lista.append(palavra)

# 4. Ordenar a lista

minha_lista.sort()

# 5. Printar na tela

print(minha_lista)