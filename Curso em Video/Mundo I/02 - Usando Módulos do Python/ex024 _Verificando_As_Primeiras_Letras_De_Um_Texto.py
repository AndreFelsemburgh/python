# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

nome_prog = ' Ex024 - Nome da Cidade '
fim = ' Fim do Programa '
print('-' * 50)
print('{:^50}' .format(nome_prog.upper()))
print('-' * 50)
Cidade = str(input('Escreva o nome da sua cidade: ')).strip()
print(Cidade[:5].upper() == 'SANTO')
print('{:-^50}' .format(fim.upper()))

