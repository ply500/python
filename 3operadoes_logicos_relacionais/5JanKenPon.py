from random import randint
from time import sleep
escolhaJogador = str(input("Escolha pedra (1), papel (2) ou tesoura (3): "))
if ((escolhaJogador == "1") or (escolhaJogador == "pedra") or (escolhaJogador == "Pedra")):
    escolhaJogador = "pedra"
    print(f"Sua escolha foi Pedra")

if ((escolhaJogador == "2") or (escolhaJogador == "papel") or (escolhaJogador == "Papel")):
    escolhaJogador = "papel"
    print(f"Sua escolha foi Papel")

if ((escolhaJogador == "3") or (escolhaJogador == "tesoura") or (escolhaJogador == "Tesoura")):
    escolhaJogador = "tesoura"
    print(f"Sua escolha foi Tesoura")

if ((escolhaJogador == "pedra") or (escolhaJogador == "papel") or (escolhaJogador == "tesoura")):

    escolhaMaquina = randint(1,3)

    if (escolhaMaquina == 1):
        if (escolhaJogador == "pedra"):
            print (f"Minha escolha também foi Pedra, deu empate!")
        elif (escolhaJogador == "papel"):
            print (f"Minha escolha foi Pedra, você ganhou!")
        else:
            print (f"Minha escolha foi Pedra, eu ganhei!")

    if (escolhaMaquina == 2):
        if (escolhaJogador == "pedra"):
            print (f"Minha escolha foi Papel, eu ganhei!")
        elif (escolhaJogador == "papel"):
            print (f"Minha escolha também foi Papel, deu empate!")
        else:
            print (f"Minha escolha foi Papel, você ganhou!")

    if (escolhaMaquina == 3):
        if (escolhaJogador == "pedra"):
            print (f"Minha escolha foi Tesoura, você ganhou!")
        elif (escolhaJogador == "papel"):
            print (f"Minha escolha foi Tesoura, eu ganhei!")
        else:
            print (f"Minha escolha também foi Tesoura, deu empate!")


else:
    print("Não entendi a sua escolha")

    #print(f"{numero}")