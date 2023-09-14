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
    print ("Já fez aniversário")
    idade = anoAtual - anoNas
elif (mesNas > mesAtual):
    print ("Ainda nã fez aniversário")
    idade = anoAtual - anoNas - 1
elif (diaNas < diaAtual):
    print ("É o mês do seu aniversário e você já fez anos")
    idade = anoAtual - anoNas
elif (diaNas == diaAtual):
    print ("Ow, feliz aniversário")
    idade = anoAtual - anoNas
else:
    print ("É o mês do seu aniversário e falta pouco")
    idade = anoAtual - anoNas - 1

if (idade < 0):
    print(f"Uau! {nome}, você ainda não nasceu!!!")
else:
    print(f"\n{nome}, você tem {idade} anos!")
