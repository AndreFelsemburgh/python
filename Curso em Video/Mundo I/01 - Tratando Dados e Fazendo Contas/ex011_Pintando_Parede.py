#Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta que precisar para pintar essa parede,
#Sabendo que cada litro de tinta pinta 2m² (Dois metros quadrados)
nome_programa = ' Pintando parede '
fim = ' fim do programa '
print('\n{:-^48}' .format(nome_programa.upper()))
alt = float(input('\nInforme a altura da parede (em metros): '))
larg = float(input('Informe a largura da parede (em metros): '))
area = alt * larg
print('Uma parede com {}m de altura por {}m de largura tem uma área de {}m² ' .format(alt, larg, area))
print('Para pintar essa parede, você precisará de {:.1f} litros de tinta.' .format( area / 2))
print('\n{:-^48}' .format(fim.upper()))