'''
10. Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo:
Média Situação
Abaixo de 3,0 Reprovado
Entre 3,0 e 6,9 Prova Final
A partir de 7,0 Aprovado
'''

nome = input("Qual seu nome ?")
nota1 = float(input("Sua nota 1:"))
nota2 = float(input("Sua nota 2:"))
media = nota1 + nota2 / 2

if(media > 7):
    print(f"Sua média é {media} situação final: APROVADO")
if(media > 3 and media < 6.9 ):
    print(f"Sua média é {media} situação final: PROVA FINAL")
if(media < 3):
    print(f"Sua media é {media} situação final: REPROVADO")