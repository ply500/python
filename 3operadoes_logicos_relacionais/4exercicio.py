from datetime import date
print("*"*20)
nome = input("Digite seu nome:")
diaNas = int(input("Digite o dia do seu nascimento:"))
mesNas = int(input("Digite o mês do seu nascimento:"))
anoNas = int(input("Digite o ano do seu nascimento:"))
diaAtual = date.today().day
mesAtual = date.today().month
anoAtual = date.today().year
#print(f"Hoje é {dataAtual} / {mesAtual} / {anoAtual}")

if (mesNas < mesAtual):
    idade = anoAtual - anoNas
else:
    if (mesNas > mesAtual):
        idade = anoAtual - anoNas - 1
    else:
        if (diaNas <= diaAtual):
            idade = anoAtual - anoNas
            if(diaNas == diaAtual):
                print ("Ow, feliz aniversário")
        else:
            idade = anoAtual - anoNas - 1

if (idade < 0):
    print(f"Uau! {nome}, você ainda não nasceu!!!")
else:
    print(f"\n{nome}, você tem {idade} anos!")
#print(date.today().year)
print(date.today())