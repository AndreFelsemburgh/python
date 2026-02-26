#Faça um programa que leia um ângulo qualquer e mostre o Seno, Cosseno e a Tangente desse ângulo.
#Com importação dos modulos sin, cos, tan e radians da biblioteca math
from math import sin, cos, tan, radians
nome_programa = ' Ex018 - Seno, Cosseno e Tangente '
fim = ' Fim do Programa '
print('\n{:-^50}' .format(nome_programa.upper()))
angulo = float(input('\nDigite o ângulo que você deseja: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))
print('O ângulo de {} tem o SENO de: {:.2f} \nO ângulo de {} tem o COSSENO de: {:.2f} \nO ângulo de {} tem a TANGENTE de: {:.2f}' .format(angulo, seno, angulo, coss, angulo, tang))
print('\n{:-^50}' .format(fim.upper()))