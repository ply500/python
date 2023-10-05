'''
1) Verifique se um determinado número se encontra na seguinte lista
[1,3,5,7,11,25,17]
Peça ao usuário digitar um número e caso número estiver na lista,
print a mensagem "Exite"

2) Contar números positivos na lista a seguir
[2,-3,-1,4,0,-9]

3) Verifique que se a lista está em ordem crescente
[1,2,3,5,7,10]
caso positivo retorne uma mensagem

4) Remova todos os numeros impares da lista a seguir
[2,9,8,9,7,10,11]
'''
import math
lista1 = [1,3,5,7,11,25,17]

numero = int(input("Digite um número inteiro: "))
achou = 0
#print(f"{numero}")
achou = lista1.count(numero)
if achou > 0:
    print("Existe")
    print(f"O número {numero} está na lista")
else:
    print("Não existe")
    print(f"O número {numero} não está na lista")

#solução 2
if numero in lista1:
    achou = 1


print("---------------------------")
lista2 = [2,-3,-1,4,0,-9]
contador = 0
for i in range (0, len(lista2)):
    #print(f"{lista2[i]}")
    numero = int(lista2[i])
    #print(f"{numero}")
    #print(type(numero))
    if (numero >= 0):
        contador += 1
print(f"Há {contador} números positivos na lista")

#solução 2
cont = 0
for num in lista2:
    if cont >= 0:
        cont += 1

print("---------------------------")
lista3 = [1,2,3,5,7,10]
lista3Temp = lista3.copy()
lista3Temp.sort()
ordemCrescente = True
for i in range (0, len(lista3)):
    if (int(lista3[i]) != int(lista3Temp[i])):
        #print(f"{lista3[i]}, {lista3Temp[i]}")
        ordemCrescente = False
if ordemCrescente:
    print("A lista está em ordem crescente")
else:
    print("A lista não está em ordem crescente")

#solução 2
if lista3 == sorted(lista3):
    print("A lista está em ordem crescente")
else:
    print("A lista não está em ordem crescente")


print("---------------------------")
lista4 = [2,9,8,9,7,10,11]
lista4Temp = lista4[:]
#print(f" copia 1 {lista4Temp}")
for i in range (0, len(lista4)):
    if (lista4[i] % 2 == 0):
        lista4Temp[i] = 0
    else:
        lista4Temp[i] = i
lista4Temp.sort(reverse=True)
#print(f" bla {lista4Temp}")
for i in range (0, len(lista4Temp)):
    if (lista4Temp[i] > 0):
        lista4.pop(lista4Temp[i])
print(lista4)

#solução 2
lista5 = [1,5,17,18,25,50]
lista_nova = [num for num in lista5 if num % 2 == 0]
print(lista_nova)
