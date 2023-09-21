candidato = int (input("Entre com um número natural não nulo: "))
#print(candidato)
run = True
divisores = 0
while (run):
    print(candidato)
    if (candidato == 1):
        print(f"O número {candidato} não é primo!")
        run = False
    elif (candidato == 2):
        print(f"O número {candidato} é primo!")
        run = False
    else:
        for i in range (2, candidato + 1):
            razao = candidato % i
            #print(f"{candidato}, {i}, {razao}")
            if(razao == 0):
                divisores += 1
                #print(f"divisore = {divisores}")
            # else:
            #     print(f"O número {candidato} não é primo!")
            #     run = False
                
        run = False

if (divisores == 1):
    print(f"O número {candidato} é primo")
else:
    print(f"O número {candidato} não é primo")

        