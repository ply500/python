nomes = ["Alice", "Bob", "Carol", "David", "Eva"]

sublista_nomes = nomes[1:4]
print("Sublista de nomes:", sublista_nomes)

print("Nomes na lista:")
for nome in nomes:
    print(nome)

nome_a_procurar = "Eva"
if nome_a_procurar in nomes:
    print(nome_a_procurar, "está na lista.")
else:
    print(nome_a_procurar, "não está na lista.")

letra_a_contagem = sum(1 for nome in nomes if nome.startswith("A"))
print("Número de nomes que começam com 'A':", letra_a_contagem)

# Crie uma lista original
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Crie uma lista vazia para armazenar a sublista
sublista = []

# Especificando os índices de início e fim da sublista
indice_inicio = 2  # O índice de início da sublista
indice_fim = 6    # O índice de fim da sublista

# Use um loop for para adicionar elementos à sublista usando append
for i in range(indice_inicio, indice_fim + 1):
    sublista.append(lista_original[i])

# Imprima a sublista resultante
print("Lista original:", lista_original)
print("Sublista:", sublista)

# Crie três sublistas
sublista1 = [1, 2, 3]
sublista2 = ['a', 'b', 'c']
sublista3 = [True, False, True]

# Crie a lista principal que contém as três sublistas
lista_principal = [sublista1, sublista2, sublista3]

# Imprima a lista principal
print("Lista Principal:", lista_principal)