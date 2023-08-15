'''
5) Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno
'''

nota1 = float(input("Sua nota 1:"))
nota2 = float(input("Sua nota 2:"))
nota3 = float(input("Sua nota 3:"))
nota4 = float(input("Sua nota 4:"))

total = (nota1 + nota2 + nota3 + nota4) / 4

if(total <= 60 ):
    print(f"APROVADO , sua media é {total}")
else:
    print("Reprovado")