# Escreva um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
nome_prog = ' Par ou Ímpar '
fim_prog = ' Fim do Programa '
print('{:-^50} ' .format(nome_prog).upper())
num = int(input('\nDigite um número: '))
if num % 2 == 0:
	print('O número {} é um número PAR' .format(num))
else:
	print('O número {} é um número IMPAR' .format(num))
print('\n{:-^50} ' .format(fim_prog).upper())