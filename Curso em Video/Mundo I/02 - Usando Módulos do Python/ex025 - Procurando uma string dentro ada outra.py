#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

program_name = ' Ex025 - Verificar Nome '
fim = ' Fim do Programa '
print('-' * 50)
print('{:^50}' .format(program_name.upper()))
print('-' * 50)
nome = str(input('Digite seu nome completo: ')).strip()
print('Existe Silva no nome? {}' .format('SILVA' in nome.upper()))
print('-' * 50)
print('{:^50}' .format(fim.upper()))
print('-' * 50)