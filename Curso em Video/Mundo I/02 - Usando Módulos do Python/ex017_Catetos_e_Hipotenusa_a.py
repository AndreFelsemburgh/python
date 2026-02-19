#17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa
#Com importação da biblioteca math
import math
nome_programa = ' Ex017 - Cálculo da Hipotenusa '
fim = ' Fim do programa '
print('\n{:=^50}' .format(nome_programa.upper()))
a = float(input('\nDigite o comprimento do cateto oposto: '))
b = float(input('Digite o comprimento do cateto adjacente: '))
h = math.sqrt(a**2 + b**2)
print('\nO valor da hipotenusa é {:.2f}' .format(h))
print('\n{:=^50}' .format(fim.upper()))