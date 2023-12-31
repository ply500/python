'''Exercício Prorama elaborado por paulo
11/09/2023q
aula 3'''

'''
1) Data de nascimento: criar um programa que pergunte ao usuário seu nome 
e a data de seu nascimento e calcule a idade com base no ano atual

2) Crie um programa em que o usuario digite os valores e o programa 
calcula a base de um triangule retangulo

3) Crie um prgrama que o usuario digite o peso e a altura e o programa calcule o IMC

4) Crie um programa em que o usuário digite um numero em graus celcius 
e o programa converte em farenheit

5) faça o mesmo para farenheit em celcius

6) crie um programa que calcule báskara dos valoes digitados
regras: a tem que ser elevado ao quadrado x2 mas a pode ter qualquer valor ax2 + ou - bx -c
'''

import math
from datetime import date
print("*"*20)
nome = input("Digite seu nome:")
#dataNas = int(input("Digite o dia do seu nascimento:"))
#mesNas = int(input("Digite o mês do seu nascimento:"))
anoNas = int(input("Digite o ano do seu nascimento:"))
print(f"\n{nome}, você tem {2023 - anoNas} anos!")
print(date.today().year)

print("*"*20)
cateto1 = float(input("Digite o valor do primeiro cateto de um triângulo retângulo em mm:").replace(",","."))
cateto2 = float(input("Digite o valor do sehundo cateto de um triângulo retângulo em mm:").replace(",","."))
print(f"\nA área do triângulo retângulo com catetos {cateto1} e {cateto2} é {((cateto1 * cateto2) / 2):.2f}mm2")

print("*"*20)
peso = float(input("Digite seu peso em kg:").replace(",","."))
altura = float(input("Digite sua antura em metros:").replace(",","."))
print(f"\nBaseado em sue peso e altura ({peso}kg e {altura} metros), seu IMC é {peso / math.pow(altura,2)}")

print("*"*20)
tempFahrenheit = float(input("Entre com a temperatura em graus Fahrenheit:").replace(",","."))
print(f"\n{tempFahrenheit}oF é igual a {(tempFahrenheit - 32) / 1.8}oC")

print("*"*20)
tempCelcius = float(input("Entre com a temperatura em graus Celcius:").replace(",","."))
print(f"\n{tempCelcius}oC é igual a {(tempCelcius * 1.8) +32}oF")

print("*"*20)
coefA = float(input("Entre com o coeficiente 'a' de uma equação de segundo grau:").replace(",","."))
coefB = float(input("Entre com o coeficiente 'b' de uma equação de segundo grau:").replace(",","."))
coefC = float(input("Entre com o coeficiente 'c' de uma equação de segundo grau:").replace(",","."))
print(f"\nA primeira raiz da equação é: {((-1*coefB) + math.sqrt(math.pow(coefB,2) - (4*coefA*coefC)))/(2*coefA)}")
print(f"A segunda raiz da equação é: {((-1*coefB) - math.sqrt(math.pow(coefB,2) - (4*coefA*coefC)))/(2*coefA)}")

print("*"*20)