#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
import random
nome_programa = ' Sorteio de aluno '
fim = ' Fim do programa '
print('\n{:-^50}' .format(nome_programa.upper()))
#Recebe dados dos usuários separados por espaço
alunos = input('\nDigite o nome dos alunos, separados por espaço: ')
#Converte a string de entrada em uma lista
lista_alunos = alunos.split()
#Escolhe um item da lista
escolhido = random.choice(lista_alunos)
print('O aluno escolhido para apagar o quadro foi {}.' .format(escolhido))
print('\n{:-^50}'.format(fim.upper()))
