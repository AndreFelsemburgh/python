#Faça um progra que leia um ano qualquer e mostre se ele é bissexto.
#import calendar
from datetime import date
np = ' Ano Bissexto? '
fp = ' Fim do Programa '
print('{:=^50}' .format(np).upper())
ano = int(input('Digite o ano que você quer consultar.\nPara consultar o ano atual, digite 0: '))
if ano == 0:
	ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
	print('O ano {} \033[1;35mé um ano bissexto\033[m.' .format(ano))
else:
	print('O ano {} \033[1;35mnão é um ano bissexto\033[m.' .format(ano))
print('\n{:=^50}' .format(fp).upper())