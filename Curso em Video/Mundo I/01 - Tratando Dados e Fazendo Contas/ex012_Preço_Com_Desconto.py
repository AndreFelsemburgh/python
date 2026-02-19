#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto 
nome_programa = ' Calcula desconto '
fim = ' fim do programa '
print('{:÷^48} \n' .format(nome_programa.upper()))
preço = float(input('Digite o preço do produto: '))
novo_preço = preço * (1 - (5/100))
print('O preço do produto com 5% de desconto será de R$ {:0.2f}.'.format (novo_preço))
print ('\n{:÷^48}' .format(fim.upper()))
