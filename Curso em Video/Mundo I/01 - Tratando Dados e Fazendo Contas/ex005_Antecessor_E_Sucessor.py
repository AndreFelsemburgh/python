#Faca um programa que leia um número inteiro e mostre na tela o seu antecessor e o seu sucessor 
tit = ('Antecessor e Sucessor')
fim = ('Fim do Programa')
print('{:-^48} \n' .format(tit))
num = int(input('Digite um número: '))
#ant = (num - 1)
#suc = (num + 1)
print('O antecessor de {} é {}.\nE o sucessor de {} é {}. \n' .format(num, (num -1), num, (num + 1)))
print('{:-^48}' .format(fim))
