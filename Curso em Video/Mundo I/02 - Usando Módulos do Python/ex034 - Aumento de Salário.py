"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um valor de 10%
Para salários iguais ou inferiores a R$ 1.250,00 o aumento é de 15%
"""
np = ' Ex034 - Aumento de Salário '
fp = ' Fim do programa '
print('{:=^50}' .format(np).upper(),'\n')
sal = float(input('Digite o valor do salário: '))
if sal > 1250:
    novo_sal = (sal * 1.1)
    print('\nPara um salário de R$ {:.2f} o aumento será de 10%. \nSeu novo salário será de \033[1;32mR$ {:.2f}\033[m' .format(sal,novo_sal))
else:
    novo_sal = (sal * 1.15)
    print('Para um salário de R$ {:.2f}, o aumento será de 15%. \nSeu novo salário será de \033[1;32mR$ {:.2f}\033[m' .format(sal, novo_sal))
print('\n{:=^50}' .format(fp).upper())