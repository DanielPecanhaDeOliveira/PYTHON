import pygame
from pygame.locals import *
from sys import exit
from random import randint
from random import choice

cores = [(128,0,128), (0,0,139), (0,191,255)]
#Inicializando modulos do  pygame
pygame.init()


#Criando a tela do game
largura = 800
altura = 720
#Gerando o nascimento da cobra
x_cobra = int(altura/2)
y_cobra = int(largura/2)
#A variável "velocidade" define a velocidade do game
velocidade = 20

x_controle = velocidade
y_controle = velocidade
#Gerando o nascimento da nossa maçã
x_maca = randint(0, 380)
y_maca = randint(0, 380)

#Escrevendo um texto que marque quantos pontos fizemos(aqui definimos somente a fonte, cor, suavizão do texto,
# para printar isso na tela do game devemos chamar mais tarde essa função dentro do loop principal)
fonte = pygame.font.SysFont('arial', 30, True, True)
fonte2 = pygame.font.SysFont('arial', 30, False, False)
pontos = 0
#Definindo o titulo da janela do game
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode((largura, altura))
#Taxa de atualização(também, será chamada mais tarde dentro do loop)
relogio = pygame.time.Clock()

lista_cobra = []
comprimemto_inicial = 5
morreu = False

#Criando função que aumenta a cobra
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x, y]
        #XeY[0] = x 
        #XeY[1] = y
        pygame.draw.rect(screen, (0, 255, 0), (XeY[0], XeY[1], 20, 20) )

def reiniciar_jogo():
    #Esta função irá zerar todas as variaveis e reiniciar o jogo
    global pontos, comprimemto_inicial, x_cobra, y_cobra, lista_cabeça, lista_cobra, x_maca, y_maca, morreu
    pontos =  0
    comprimemto_inicial = 5
    x_cobra = int(altura/2)
    y_cobra = int(largura/2)
    lista_cabeça = []
    lista_cobra = []
    x_maca = randint(0, 380)
    y_maca = randint(0, 380)
    morreu = False


#Criando loop principal
while True:
    relogio.tick(10)
    screen.fill((255, 255, 255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    
    #Checando se algum evento ocorreu
    for event in pygame.event.get():
        #Checando se o evento for do tipo 'sair'
        if event.type == QUIT:
            pygame.QUIT
            exit()
        #Checando qual tecla o usuário vai clicar
        if event.type == KEYDOWN:
            if event.key == K_a:
                #Cada verifi... 'x_controle' verifica para qual lado a cobra está indo e bloqueia a direção oposta 
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle  = 0 
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade 
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    #Criando cabeça da cobra
    lista_cabeça = []
    lista_cabeça.append(x_cobra)
    lista_cabeça.append(y_cobra)
    
    #Criando o corpo da cobra 
    lista_cobra.append(lista_cabeça)
    #Se as posições da cabeça forem maiores que um ou seja, duplicadas significa que a cobra bateu nela mesma e morreu
    if lista_cobra.count(lista_cabeça) > 1:
        morreu = True
        while morreu:
            screen.fill((255, 255, 255))
            mensagem = 'GAME OVER! Aperte a tecla R para jogaar novamente' 
            texto_formatado2 = fonte2.render(mensagem, True, (0, 0, 0))
            rect_texto = texto_formatado2.get_rect()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            rect_texto.center = (largura//2, altura//2)
            screen.blit(texto_formatado, (240, 20))
            screen.blit(texto_formatado2, rect_texto)
            pygame.display.update()
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra  > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura

    #Devemos definir um tamanho para nossa cobra inicialmente, se não fizermos isso a nossa cobra vai crescer sem parar antes mesmo de acertar o alvo 'maçã'
    if len(lista_cobra)> comprimemto_inicial:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)

    #Desenhando nossa cobra e maçã na tela
    cobra = pygame.draw.rect(screen, (0, 255, 250), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(screen, choice(cores), (x_maca, x_maca, 20, 20))
    
    #Criando colisão da cobra com a maçã
    if cobra.colliderect(maca):
        x_maca = randint(0, 380)
        y_maca = randint(0, 380)
        pontos = pontos + 1
        comprimemto_inicial = comprimemto_inicial + 5

    screen.blit(texto_formatado, (240, 20))
    pygame.display.update()

