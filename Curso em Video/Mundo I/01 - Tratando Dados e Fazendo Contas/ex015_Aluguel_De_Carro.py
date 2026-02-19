#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calculo o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado.
nome_programa = ' Aluguel de carro '
fim = ' fim do programa '
sep = '|'
print('{:-^48}' .format(nome_programa.upper()))
qtdDias = int(input('\nQuantos dias de aluguel? '))
kmRodados = float(input('Quantos km rodados? '))
valor_km = kmRodados * 0.15
valor_dias = qtdDias * 60
total = valor_km + valor_dias
print('O valor total a ser pago pelo aluguel do carro, \nserá de: R$ {:.2f}.' .format(total))
print('\n{:-^48}' .format(fim.upper()))
