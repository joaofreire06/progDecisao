'''
1. Fazer um algoritmo que peça um número, e ao final, informe se o número digitado está acima de 1000 ou
abaixo de 1000.
'''

num = int(input("Informe um número:"))

if(num < 1000):
    print(f"{num} está abaixo de 1000")
else:
    print(f"{num} está acima de 1000")