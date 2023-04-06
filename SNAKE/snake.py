import pygame
#Inicializando módulos de Pygame
pygame.init()

#Criando uma janela com o titulo "Snake"
janela = pygame.display.set_caption('Snake')
#Definindo tamanho da tela 
pygame.display.set_mode((400, 300))

loop = True
#Loop do jogo
while loop:
    #Checando eventos
    for event in pygame.event.get():
        #Se for um evento QUIT('Saida')
        if event.type == pygame.QUIT:
            loop = False
#Encerrando módulos de Pygame
pygame.quit()
