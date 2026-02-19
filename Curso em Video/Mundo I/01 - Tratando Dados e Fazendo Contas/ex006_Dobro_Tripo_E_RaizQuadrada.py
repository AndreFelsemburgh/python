#Crie um algoritmo que leia um número e mostre o seu dobro, o triplo e a raiz quadrada.
tit = (' Dobro, Triplo e Raiz Quadrada ')
fim = (' Fim do Programa ')
print('{:-^48} \n' .format(tit))
num = int(input('Digite um número: '))
print('O dobro de {} é: {}' .format(num, num * 2),'\nO triplo de {} é: {}' .format(num, num * 3), '\nE a Raiz Quadrada de {} é: {:.2f} ' .format(num, pow(num, (1/2))), '\n')
print('{:-^48}' .format(fim))
