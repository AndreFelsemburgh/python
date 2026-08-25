"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
Ex.: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""
program_name = ' Ex027 - Primeiro e último nome '
fim = ' Fim do programa '
print('-' * 50)
print('{:^50} ' .format(program_name.upper()))
print('-' * 50)
nomeCompleto =str(input('Digite seu nome completo: ')).strip()
lista_nome = nomeCompleto.split()
print('Seu primeiro none é {}' .format(lista_nome[0]))
print('Seu último nome é {}' .format(lista_nome[len(lista_nome)-1]))
print('-' * 50)
print('{:^50} ' .format(fim.upper()))
print('-' * 50)