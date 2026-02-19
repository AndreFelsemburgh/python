#Crie um programa que leia quanto uma pessoa tem de dinheiro e quantos dólares ela pode comprar
#US$ 1,00 = R$ 3,27
nome_programa = ' Conversor de Moeda '
fim = ' fim do programa '
print('\n{:-^48} ' .format(nome_programa.upper()))
valor = float(input('\nQuanto dinheiro você tem na carteira? R$ '))
print('\nCom R$ {:.2f}, você consegue comprar US$ {:.2f}.' .format(valor, valor/3.27))
print('\n{:-^48}' .format(fim.upper()))
