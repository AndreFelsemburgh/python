# Faca um programa que leia 3 números e mostre qual é o maior e qual é o menor
np = ' Ex033 - Maior e Menor '
fp = ' Fim do programa '
print('{:-^50}' .format(np).upper())
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
menor = n1
if n2< n3 and n2 < n1:
	menor = n2
if n3 < n1 and n3 < n2:
	menor = n3
maior = n2
if n1 > n2 and n1 > n3:
	maior = n1
if n3 > n1 and n3 > n2:
	maior = n3
	
print('\nO menor número digitado foi \033[1;32m{}\033[m ' .format(menor))
print('O maior número digitado foi \033[1;32m{}\033[m' .format(maior))
	
print('\n{:-^50}' .format(fp).upper())