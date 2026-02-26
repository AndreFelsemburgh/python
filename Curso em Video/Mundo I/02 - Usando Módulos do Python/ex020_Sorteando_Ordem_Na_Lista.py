#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle, sample
nome_programa = ' Ex020 - Sorteando Ordem Na Lista '
fim = ' Fim do programa '
print('\n{:=^50}' .format(nome_programa.upper()))
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos) #shuffle embaralha a lista, que neste caso é alunos
print('\nA ordem de apresentação do trabalho é: \n {}' .format(alunos))
print('\n{:=^50}' .format(fim.upper()))
'''
ordem = sample(alunos, len(alunos)) #Se queremos utilizar a lista inteira, podemos usar len(alunos), pois ele vai utilizar toda a lista como referência
ordem = sample(alunos, k=4) #Usamos o K para definirmos a quantidade de itens que queremos escolher.
print('A ordem de apresentação do trabalho é: \n {}' .format(ordem))
'''




