'''
5. Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

sigla = input("Informe a sigla de um estado brasileiro:")
str = 'SP'
est = 'RJ'
est1 = 'MG'
est2 = 'ES'

if(sigla == str):
    print("O estado está na região Sudeste")
if(sigla == est):
    print("O estado está na região Sudeste")
if(sigla == est1):
    print("O estado está na região Sudeste")
if(sigla == est2):
    print("O estado está na região Sudeste")
if(sigla != str and sigla != est and sigla != est1 and sigla != est2):
    print("O estado não está na região Sudeste")
