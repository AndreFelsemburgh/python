"""
Faça um programa que leia uma frase pelo teclado e mostre:
 - Quantas vezes aparece a letra "A"
 - Em que posição ela aparece a primeira vezes
 - Em que posição ela aparece a última vezes
"""

program_name = ' Ex026 - Contador de letras '
fim = ' Fim do Programa '
print('-' * 50)
print('{:^50}' .format(program_name.upper()))
print('-' * 50)
frase = str(input('Digite uma frase: ')).strip()
print('Qtd de letras "A" na frase: {} ' .format(frase.lower().count('a')))
print('A primeira posição da letra é a {} ' .format(frase.lower().find('a')+1))
print('A ultima posição da letra é a {} ' .format(frase.lower().rfind('a')+1))
print('-' * 50)
print('{:^50}' .format(fim.upper()))
print('-' * 50)