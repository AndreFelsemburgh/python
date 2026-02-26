#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
import random
nome_programa = ' Sorteio de aluno '
fim = ' Fim do programa '
print('\n{:-^50}' .format(nome_programa.upper()))
#Recebe dados dos usuários
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
#Cria uma lista, entre colchetes [....] pois o random.choice precisa escolher os nomes de uma lista
alunos = [aluno1, aluno2, aluno3, aluno4]
#Escolhe um item da lista
escolhido = random.choice(alunos)
print('\nO aluno escolhido para apagar o quadro foi {}.' .format(escolhido))
print('\n{:-^50}'.format(fim.upper()))
