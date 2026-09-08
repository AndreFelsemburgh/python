"""
Escreva um programa que leia a velocidade de um carro.
Sa ala ultrapassar 80Km/h, mostra uma mensagem dizendo que ele foi multado.
A multa vai custar R$7.00 por cada Km acima do limite.
"""
nome_prog = ' Velocidade e Multa '
fim_prog = ' Fim do programa '
print('{:-^50}' .format(nome_prog).upper())
vel = float(input('Qual a velocidade do carro? '))
vel_exc = float(vel - 80)
valor_multa =  float(vel_exc * 7)
if vel <= 80:
	print('Parabéns! Você é um motorista prudente e não receberá multa!')
else:
	print('Voce excedeu o limite de velocidade em {} km/h. \nVocê foi multado e pagará R$ {:.2f} ' .format(vel_exc, valor_multa))
print('{:-^50}' .format(fim_prog).upper())