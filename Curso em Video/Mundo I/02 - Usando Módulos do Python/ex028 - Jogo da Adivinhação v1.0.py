"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuãrio tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu
"""
import random
nome_programa = ' Ex028 - Jogo da Adivinhação v1.0 '
fim_prog = ' Fim do progama '
num_comp = random.randint(0,5)
print('{:-^50} \n' .format(nome_programa).upper())
print('O computador pensou em um número entre 0 e 5.\nTente adivinhar!')
num_usuario = int(input('Qual numero o computador pensou? '))
print('Você digitou o n° {} e o computador pensou no n° {}' .format(num_usuario, num_comp))
if num_usuario ==  num_comp:
	print('Parabéns! Você venceu!')
else: 
	print('Que pena, você perdeu! Tente novamente!')
print('\n{:-^50}' .format(fim_prog).upper())