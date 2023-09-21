soma = 0
i = 1
while True:
    nota = float(input(f"Digite a nota {i}: ").replace(",","."))
    soma += nota

    sair = ""
    while (sair != "S") or (sair != "N"):
        sair = str(input("Quer sair do programa [S] ou [N]?: ").upper().strip()[0])
        if sair == "S":
            print(sair)
            break
        elif sair == "N":
            print(sair)
            break
            

    if sair == "S":
        print(sair)
        break
    elif sair == "N":
        print(sair)
        #continue

    i += 1
media = soma / i
print(f"A média dos {i} valores é: {media:.2f}")