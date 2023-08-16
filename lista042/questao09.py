'''
9. Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final, informe na tela se a pessoa é menor de
idade, se é maior de idade, ou se é maior de 65 anos
'''

idade = int(input("Qual sua idade ?"))

if(idade < 18):
    print("Você é menor de idade!")
if(idade >= 18):
    print("Você é maior de idade!")
if(idade >= 65):
    print("Maior de 65 anos")