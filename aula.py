import sys
import pygame
import random

pygame.init()

#Configuração da tela
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

PRETO = (0, 0, 0)
BRANCO = (244, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AMARELO = (255, 255, 0)

tamanho_fonte = 50
fonte =pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("Maria", True, BRANCO)

texto_rect = texto.get_rect(center=(largura / 2, altura / 2))
clock = pygame.time.Clock()

#velocidade_x = 1
#velocidade_y = 1

velocidade_x = random.randint(-1, 1)
velocidade_y = random.randint(-1, 1)

while velocidade_x == 0:
    velocidade_x = random.randint(-1, 1)
while velocidade_y == 0:
    velocidade_y = random.randint(-1, 1)


#Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    texto_rect.x += velocidade_x

    if texto_rect.right >= largura:
        velocidade_x = random.randint(-1, 0)
        velocidade_y = random.randint(-1, 1)
        texto = fonte.render("Maria", True, VERMELHO)

    if texto_rect.left <= 1:
        velocidade_x = random.randint(0, 1)
        velocidade_y = random.randint(-1, 1)
        texto = fonte.render("Maria", True, VERDE)
    
    texto_rect.y += velocidade_y

    if texto_rect.bottom <= 1:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(-1, 1)
        texto = fonte.render("Maria", True, AMARELO)

    if texto_rect.top >= altura:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(-1, 1)
        texto = fonte.render("Maria", True, AZUL)


    clock.tick(120)
    tela.fill(PRETO)
    tela.blit(texto, texto_rect)
    pygame.display.flip()