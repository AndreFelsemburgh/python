#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do Seno, Cosseno e a Tangente desse ângulo.
#Com importação da biblioteca math
import math
nome_programa = ' Ex018 - Seno, Cosseno e Tangente '
fim = ' Fim do Programa '
print('\n{:-^50}' .format(nome_programa.upper()))
angulo = float(input('\nDigite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O ângulo de {} tem o SENO de: {:.2f} \nO ângulo de {} tem o COSSENO de: {:.2f} \nO ângulo de {} tem a TANGENTE de: {:.2f}' .format(angulo, seno, angulo, cos, angulo, tang))
print('\n{:-^50}' .format(fim.upper()))