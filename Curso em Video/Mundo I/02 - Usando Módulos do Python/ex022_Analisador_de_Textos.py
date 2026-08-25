# Crie m programa que leia o nome completo de uma pessoa e mostre:
"""
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras tem ao todo (sem espaços)
- Quantas letras tem o primeiro nome
"""

nome_prog = ' Ex022 - Analisador de Textos '
fim = ' Fim do Programa '
print('-' * 50)
print('{:^50}' .format(nome_prog.upper()))
print('-' * 50)
nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
total_letras = "".join(nome.split())
print('Quantidade de letras no nome: {} ' .format(len(total_letras)))
lista_nome = nome.split()
print('Quantidade de letras do primeiro nome: {} ' .format(len(lista_nome[0])))
print('{:-^50}' .format(fim.upper()))

