#Faca um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
nome_programa = ' Reajuste Salarial '
fim = ' fim do programa '
print('\n{:-^48}' .format(nome_programa.upper()))
salário = float(input('\nSalário: R$ '))
reajuste = salário * (1 + (15 / 100))
print('O valor do novo salário com reajuste de 15% será de: R$ {:.2f}' .format (reajuste))
print ('\n{:-^48}' . format(fim.upper()))
