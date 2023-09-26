import random
escolhaJogador = str(input("Escolha ímpar (1) ou par (2): "))
numeroJogador = int(input("Entre com um número entre 1 a 1000: "))
if ((escolhaJogador == "1") or (escolhaJogador == "ímpar") or (escolhaJogador == "Ímpar") or (escolhaJogador == "Impar") or (escolhaJogador == "impar")):
    escolhaJogador = "impar"
    print(f"Sua escolha foi ímpar e o número foi {numeroJogador}")
elif ((escolhaJogador == "2") or (escolhaJogador == "par") or (escolhaJogador == "Par") or escolhaJogador == "par"):
    escolhaJogador = "par"
    print(f"Sua escolha foi par e o número foi {numeroJogador}")
else:
    print ("Escolha inválida...")

print("Sorteando número para mim...")
numeroMaquina = random.randint(1, 1000)
print(f"Meu número é {numeroMaquina}")

soma = numeroJogador + numeroMaquina

if (soma % 2 == 0):
    print (f"A soma dos dois números é {soma} e é par!")
    if (escolhaJogador == "par"):
        print("Parabéns, Você ganhou!!!")
    else:
        print("Eu ganhei!!!")

if (soma % 2 == 1):
    print(f"A soma dos dois números é {soma} e é ímpar!")
    if (escolhaJogador == "impar"):
        print("Parabéns, Você ganhou!!!")
    else:
        print("Eu ganhei!!!")

