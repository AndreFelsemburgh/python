"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separaos
Ex: Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
"""

nome_prog = ' Ex023 - Analisando Números '
fim = ' Fim do Programa '
print('-' * 50)
print('{:^50}' .format(nome_prog.upper()))
print('-' * 50)
numero = int(input('Digite um número entre 0 e 9999: '))
un = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10
print('Unidade: {} ' .format(un))
print('Dezena: {} ' .format(dez))
print('Centena: {} ' .format(cen))
print('Milhar: {} ' .format(mil))
print('{:-^50}' .format(fim.upper()))

