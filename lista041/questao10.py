'''
10) Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado
'''

in1 = int(input("Informe um número inteiro:"))
in2 = int(input("Informe outro número inteiro:"))

if(in1 // in2):
    print(f"O número {in2} é divisor")
else:
    print(f"O número {in2} não é divisor")