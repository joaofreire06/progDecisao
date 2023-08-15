'''
8) Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10
'''

num = int(input("Informe um número:"))

if(num > 1 and num <= 10):
    print(f"O número {num} está entre 1 e 10")
else:
    print(f"O número {num} não está entre 1 e 10")