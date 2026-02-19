#Escreva um programa que converta um temperatura digitada em ºCelsius para ºFarenheit
nome_programa = ' Conversor de temperatura '
fim = ' fim de programa '
print('\n{:-^48}' .format(nome_programa.upper()))
grausC = float(input('\nInforme a temperatura em ºCelsius: '))
grausF =  (grausC * 9 / 5) + 32
print('A temperatura de {:.1f}ºC corresponde a {:.2f}ºF!'. format(grausC, grausF))
print('\n{:-^48}' .format(fim.upper()))
