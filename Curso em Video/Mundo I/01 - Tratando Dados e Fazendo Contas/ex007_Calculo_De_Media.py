#Desenvolva um programa que leia 2 notas de um aluno, calcule e mostre a sua média
tit = (' Cálculo de Média ')
fim = (' Fim do Programa ')
print('{:-^48}' .format(tit.upper()))
nota1 = float(input('\nDigite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = ((nota1 + nota2) / 2)
print('A média entre {} e {} é igual a: {:.1f}' .format(nota1, nota2, media), '\n')
print('{:-^48}' .format(fim.upper()))
