'''
7. Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais.
'''

num1 = int(input("Informe um número:"))
num2 = int(input("Informe outro número:"))

if(num1 > num2):
    print(f"{num1} é maior,{num2} é o menor")
if(num2 > num1):
    print(f"{num2} é maior,{num1} é o menor")
if(num1 == num2):
    print("Ambos são iguais!")