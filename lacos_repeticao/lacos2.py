'''Exercício programa para cálculo de média de 4 valores'''
soma = 0
for i in range (1,5):
    nota = float(input(f"Digite a nota {i}: ").replace(",","."))
    soma += nota
    #print(f"A soma parcial é: {soma}")
media = soma / 4
print(f"A média dos 4 valores é: {media:.2f}")