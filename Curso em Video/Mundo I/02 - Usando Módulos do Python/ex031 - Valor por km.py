"""
Desenvolva um programa que pargunta a distância de uma viagem em Km. Calcula o preço da passagem.cobrando R$0.50 por Km para viagens de até 200Km a R$0.45 para viagens mais longas.
"""
np = ' Preço da passagem '
fp = ' Fim do programa '
print('{:-^50}' .format(np).upper())
dist = float(input('Qual a distância da viagem, em Km? '))
if dist <= 200:
	valor = (dist * 0.50)
	print('O valor da passagem para uma distância de {} km, será de R$ {:.2f}' .format(dist,valor))
else:
	valor = (dist * 0.45)
	print('O valor da passagem para uma distância de {} km, será de R$ {:.2f}' .format(dist,valor))
print('\n{:-^50}' .format(fp).upper())