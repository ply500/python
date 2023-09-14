moeda = True
ponto = 0
nome = str(input("Nome do personagem: "))
if (nome == "Mario" and moeda == True):
    ponto = ponto + 1
    print(f"{nome} pegou a moeda e teve {ponto} ponto")
else:
    print("Não pegou a moeda")
