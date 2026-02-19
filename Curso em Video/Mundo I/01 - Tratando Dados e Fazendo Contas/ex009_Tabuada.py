#Crie um programa que leia um número inteiro qualquer e exiba na tela a sua tabuada.
nome_programa = ' Tabuada '
fim = ' Fim do programa '
print('{:-^48}' .format(nome_programa.upper()))
num = int(input('\nDigite um número para obter a sua tabuada: '))
print('\nA tabuada de {} é:' .format(num))
print('-' * 12)
print('{} x {:2} = {}'.format(num, 1, num * 1))
print('{} x {:2} = {}'.format(num, 2, num *2))
print('{} x {:2} = {}'.format(num, 3, num * 3))
print('{} x {:2} = {}'.format(num, 4, num * 4))
print('{} x {:2} = {}'.format(num, 5, num * 5))
print('{} x {:2} = {}'.format(num, 6, num * 6))
print('{} x {:2} = {}'.format(num, 7, num * 7))
print('{} x {:2} = {}'.format(num, 8, num * 8))
print('{} x {:2} = {}'.format(num, 9, num * 9))
print('{} x {:2} = {}'.format(num, 10, num * 10) )
print('-' * 12)
print('\n{:-^48}' .format(fim.upper()))
