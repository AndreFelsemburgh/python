import pygame
nome_programa = ' Ex021 - Tocando um MP3 '
fim = ' Fim do programa '
print('-' * 50)
print('{:^50}' .format(nome_programa.upper()))
print('-' *50)
pygame.init() #inicia o pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021fundo.mp3') #Carrega o arquivo mp3
pygame.mixer.music.play() #Toca a música.
pygame.event.wait() #Espera o evento (A musica) terminar para fechar o programa
print('Tocando a música')
input('Pressione <enter> interromper a música: ')
print('Música interrompida!')
print('-' * 50)
print('{:^50}' .format(fim.upper()))
print('-' *50)