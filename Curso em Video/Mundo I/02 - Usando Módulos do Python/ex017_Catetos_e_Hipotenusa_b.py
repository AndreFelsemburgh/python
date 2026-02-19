#17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa
#Com importação apenas do método hypot
from math import hypot
nome_programa = ' Ex017 - Cálculo da Hipotenusa '
fim = ' Fim do programa '
print('\n{:=^50}' .format(nome_programa.upper()))
a = float(input('\nDigite o comprimento do cateto oposto: '))
b = float(input('Digite o comprimento do cateto adjacente: '))
h = hypot(a,b)
print('\nO valor da hipotenusa é {:.2f}' .format(h))
print('\n{:=^50}' .format(fim.upper()))