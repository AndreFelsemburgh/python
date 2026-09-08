"""
Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.
Dados três segmentos eles formam um triângulo se: a+ b > c  //  a + c > b  //  b + c > a
"""
np = ' Ex035 - Analise de triangulo '
fp = ' Fim do Programa '
print('{:=^50}' .format(np).upper())
reta1 = float(input('\nDigite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))
if (reta1 + reta2) > reta3 and (reta2+reta3) > reta1 and (reta3 + reta1) > reta2:
	print('Essas retas \033[1;34mformam um triângulo\033[m.')
else:
	print('Essas retas \033[1;34mnão formam un triângulo\033[m.')
print('\n{:=^50}' .format(fp).upper())