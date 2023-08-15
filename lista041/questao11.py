'''
11) Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas
'''

num1 = int(input("informe um número que possua 3 algarismos:"))

if(num1 >= 100 and num1 <= 999):
    centena = num1 // 100
    print(f"O algarismo das centenas de {num1} é {centena}")
else:
    print(f"O valor informado não possui 3 algarismos")