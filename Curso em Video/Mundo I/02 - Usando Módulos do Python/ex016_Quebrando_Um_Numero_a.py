#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
import math
nome_programa = ' Ex016 - Quebrando um número '
fim = ' Fim do programa '
print('\n{:-^50}' .format(nome_programa.upper()))
num = float(input('\nDigite um número real: '))
print('A parte inteira de {} é: {}' .format(num, math.trunc(num)))
print('\n{:-^50}' .format(fim.upper()))