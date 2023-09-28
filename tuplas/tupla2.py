nome = ("Bla", "Ble", "Bli", "Blo", "Blu")

for valor in nome:
    print(valor)

print("============")
for chave, valor in enumerate(nome):
    print(f"chave = {chave} e valor = {valor}")

print("============")
for chave, valor in enumerate(nome):
    print(f"chave = {chave} e valor = {valor}")
    for key, value in enumerate(valor):
        print(f"key = {key} e value = {value}")

print("============")
vetA = (2,5,6,4,2,3)
vetB = (3,4,5,6,8,2)
for valorA in vetA:
    for valorB in vetB:
        mult = valorA * valorB
        print(f"{valorA} * {valorB} = {mult}")
    print("\n")
