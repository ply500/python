from random import choice
from random import randint
from time import sleep

empate = 0
vitoria = 0
derrota = 0
jogador = 0
computador = 0
animal = ["🐻 Urso", "🦅 Águia", "🐺 Lobo"]

fraseUrso = ["Quero mel", "Preciso hibernar", "Hurray to Theodore Roosevelt"]
fraseAguia = ["Tio Sam", "De cima eu te enxergo melhor", "Vai Curintia"]
fraseLobo = ["Dança comigo", "Homem é o lobo do homem", "Auuu"]

print("======================")
print("ESCOLA DE MAGIA PYTHON")
print("======================\n")

run = True
while run:
    menuEscolha = input('''*** MENU do JOGO ***
[1] Tranformar em um animal 
[2] Jogo druídico 
[3] Conversar com o animal
[4] Sair do jogo
                        
Faça sua escolha: ''')
    print("\n")
    
    if menuEscolha not in ["1", "2", "3", "4"]:
        print("Escolha inválida, tente novamente...\n")
    else:
        menuEscolha = int(menuEscolha)

    match menuEscolha:
        case 1:
            escolhendoAnimal = True
            while escolhendoAnimal:
                jogador = input ('''*** MENU de BICHOS ***
[1] 🐻 Urso 
[2] 🦅 Águia 
[3] 🐺 Lobo
                        
Faça sua escolha: ''')
                if jogador not in ["1", "2", "3"]:
                    print("Escolha inválida, tente novamente...\n")
                else:
                    jogador = int(jogador)
                    print("transmutando em 3")
                    sleep(1)
                    print("transmutando em 2")
                    sleep(1)
                    print("transmutando em 1")
                    sleep(1)
                    print(f"Você se transmutou em um {animal[jogador - 1]}\n")
                    escolhendoAnimal = False
            
        case 2:
            if jogador == 0:
                print("Escolha um animal antes...\n")
            else:
                computador = randint(1,3)
                print("Invocando um adversário")
                sleep(1)
                print("🐻")
                sleep(1)
                print("🦅")
                sleep(1)
                print("🐺")
                sleep(1)
                
                print(f"Um {animal[computador - 1]} foi invocado")
                sleep(1)
                print("🎆 POW")
                sleep(1)
                print("💣 PAFF")
                sleep(1)
                print("🧨 BUMM")
                sleep(1)

                if jogador == 1:
                    if computador == 1:
                        print (f"Você se transmutou em {animal[jogador - 1]} e o seu adversário invocou um {animal[computador - 1]}")
                        print ("Deu empate...\n")
                        empate += 1
                        print(f"Até o momento você tem {vitoria} vitórias, {empate} empates e {derrota} derrotas")
                    elif computador == 2:
                        print (f"Você se transmutou em {animal[jogador - 1]} e o seu adversário invocou um {animal[computador - 1]}")
                        print("Você perdeu...\n")
                        derrota += 1
                        print(f"Até o momento você tem {vitoria} vitórias, {empate} empates e {derrota} derrotas")
                    elif computador == 3:
                        print (f"Você se transmutou em {animal[jogador - 1]} e o seu adversário invocou um {animal[computador - 1]}")
                        print("Você ganhou...\n")
                        vitoria += 1
                        print(f"Até o momento você tem {vitoria} vitórias, {empate} empates e {derrota} derrotas")
                    else:
                        print("Alguma coisa não está certa...\n")    
                elif jogador == 2:
                    if computador == 1:
                        print (f"Você se transmutou em {animal[jogador - 1]} e o seu adversário invocou um {animal[computador - 1]}")
                        print("Você ganhou...\n")
                        vitoria += 1
                        print(f"Até o momento você tem {vitoria} vitórias, {empate} empates e {derrota} derrotas")
                    elif computador == 2:
                        print (f"Você se transmutou em {animal[jogador - 1]} e o seu adversário invocou um {animal[computador - 1]}")
                        print ("Deu empate...\n")
                        empate += 1
                        print(f"Até o momento você tem {vitoria} vitórias, {empate} empates e {derrota} derrotas")
                    elif computador == 3:
                        print (f"Você se transmutou em {animal[jogador - 1]} e o seu adversário invocou um {animal[computador - 1]}")
                        print("Você perdeu...\n")
                        derrota += 1
                        print(f"Até o momento você tem {vitoria} vitórias, {empate} empates e {derrota} derrotas")
                    else:
                        print("Alguma coisa não está certa...\n")    
                elif jogador == 3:
                    if computador == 1:
                        print (f"Você se transmutou em {animal[jogador - 1]} e o seu adversário invocou um {animal[computador - 1]}")
                        print("Você perdeu...\n")
                        derrota += 1
                        print(f"Até o momento você tem {vitoria} vitórias, {empate} empates e {derrota} derrotas")
                    elif computador == 2:
                        print (f"Você se transmutou em {animal[jogador - 1]} e o seu adversário invocou um {animal[computador - 1]}")
                        print("Você ganhou...\n")
                        vitoria += 1
                        print(f"Até o momento você tem {vitoria} vitórias, {empate} empates e {derrota} derrotas")
                    elif computador == 3:
                        print (f"Você se transmutou em {animal[jogador - 1]} e o seu adversário invocou um {animal[computador - 1]}")
                        print ("Deu empate...\n")
                        empate += 1
                        print(f"Até o momento você tem {vitoria} vitórias, {empate} empates e {derrota} derrotas")
                    else:
                        print("Alguma coisa não está certa...\n")
                else:
                    print("Alguma coisa não está certa...\n")
           
        case 3:
            match jogador:
                case 1:
                    print(choice(fraseUrso))
                    print("\n")
                case 2:
                    print(choice(fraseAguia))
                    print("\n")
                case 3:
                    print(choice(fraseLobo))
                    print("\n")
                case _:
                    print("Transmute-se em um animal antes...\n")  
        case 4:
            print("Saindo da ESCOLA DE MAGIA PYTHON")
            run = False;
    #run = 0
