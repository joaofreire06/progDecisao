'''
4. Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana
'''

dia = int(input("Informe um número de 1 a 7:"))

if(dia == 1):
    print("Domingo")
if(dia == 2):
    print("Segunda-Feira")
if(dia == 3):
    print("Terça-Feira")
if(dia == 4):
    print("Quarta-Feira")
if(dia == 5):
    print("Quinta-Feira")
if(dia == 6):
    print("Sexta-Feira")
if(dia == 7):
    print("Sábado")
if(dia > 7):
    print("Número inválido")