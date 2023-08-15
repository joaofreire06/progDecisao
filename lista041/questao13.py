'''
13) Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente
'''

a = int(input("Informe um valor:"))
b = int(input("Informe um valor:"))
c = int(input("Informe um valor:"))

# 1- a tem que ser menor que b
if(a > b):
    aux = a
    a = b
    b = aux
#garantindo até aqui entre a e b, omenor está em a
#2- a tem que ser menor que c

if(a > c):
    aux = c
    a = c
    c = aux

#garantindo ate aqui que a é menor dos 3
# agora é necessario garantir que b seja menor que c

if(b > c):
    aux = b
    b = c
    c = aux
# garantido até aqui entre b e c , o b é menor , ou seja, o c é o maior de todos

print(f"Ordem crescente: {a},{b} e {c}")