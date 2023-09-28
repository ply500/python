nomeLista1 = ["Bla", "Ble", "Bli", "Blo", "Blu"]
nomeLista2 = ["Cla", "Cle", "Cli", "Clo", "Clu"]
print("nomeLista1")
print(nomeLista1)
print("nomeLista2")
print(nomeLista2)

print("---------------------------")
print("append insere um item no fim da lista")
nomeLista1.append("Glasglow")   
print(nomeLista1)

print("---------------------------")
print("extend insere uma lista na outra")
nomeLista1.extend(nomeLista2)   
nomeLista2.extend(["Dla", "Dle", "Dli", "Dlo", "Dlu"])   
print(nomeLista1)
print(nomeLista2)

print("---------------------------")
print("insert insere um item em determinada posição")
nomeLista1.insert(3, "The Forth")   
print(nomeLista1)

print("---------------------------")
print("remove procura um item na lista e remove o primeiro que encontrar")
nomeLista1.remove("Ble")   
print(nomeLista1)

print("---------------------------")
print("pop remove e retorna um item em determinada posição")
item = nomeLista1.pop(3)
print(f"{item} foi removido")
print(nomeLista1)

print("---------------------------")
print("clear apaga todos os itens da lista")
nomeLista1.clear()
print(nomeLista1)

nomeLista1 = ["Bla", "Ble", "Bli", "Blo", "Blu"]
print("---------------------------")
print("clear apaga todos os itens da lista")
nomeLista1.clear()
print(nomeLista1)
