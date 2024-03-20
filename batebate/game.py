# Importa as bibliotecas necessárias
import pygame
import macmovimento  # Módulo contendo as classes Paddle e Ball

class Game:
    def __init__(self):
        pygame.init()  # Inicializa o Pygame
        # Configurações da tela e inicialização de objetos
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))  # Cria a janela do jogo
        self.clock = pygame.time.Clock()  # Relógio para controle de frames
        self.running = True  # Flag para indicar se o jogo está em execução
        # Raquete controlada pelo PC à esquerda (IA)
        self.paddle_left = macmovimento.Paddle(30, self.screen_height / 2 - 50, None, None)  # IA, teclas não necessárias
        # Raquete controlada pelo jogador à direita
        self.paddle_right = macmovimento.Paddle(self.screen_width - 50, self.screen_height / 2 - 50, pygame.K_UP, pygame.K_DOWN)
        self.ball = macmovimento.Ball(self.screen_width / 2, self.screen_height / 2)  # Bola no centro da tela

    def run(self):
        # Loop principal do jogo
        while self.running:
            for event in pygame.event.get():  # Processa eventos do Pygame
                if event.type == pygame.QUIT:  # Verifica se o evento é de saída (fechar janela)
                    self.running = False  # Encerra o loop principal
            
            # Movimenta a raquete controlada pela IA
            self.move_pc_paddle()
            # Movimenta a raquete controlada pelo jogador
            self.paddle_right.move(self.screen_height)
            # Movimenta a bola
            self.ball.move()
            # Verifica colisões com as raquetes
            self.ball.check_collision(self.paddle_left)
            self.ball.check_collision(self.paddle_right)

            # Limpa a tela com uma cor de fundo
            self.screen.fill((0, 0, 0))
            # Desenha os objetos na tela
            self.paddle_left.draw(self.screen)
            self.paddle_right.draw(self.screen)
            self.ball.draw(self.screen)

            # Atualiza a tela
            pygame.display.flip()
            # Define a taxa de atualização (60 quadros por segundo)
            self.clock.tick(60)

        pygame.quit()  # Encerra o Pygame ao sair do loop principal

    def move_pc_paddle(self):
        # Lógica para movimentar a raquete controlada pela IA em direção à bola
        if self.ball.rect.centery > self.paddle_left.rect.centery:
            # Move para baixo se a bola estiver abaixo da raquete
            self.paddle_left.rect.y += min(self.ball.rect.centery - self.paddle_left.rect.centery, self.paddle_left.speed)
        elif self.ball.rect.centery < self.paddle_left.rect.centery:
            # Move para cima se a bola estiver acima da raquete
            self.paddle_left.rect.y -= min(self.paddle_left.rect.centery - self.ball.rect.centery, self.paddle_left.speed)

        # Limita o movimento da raquete para que não saia da tela
        self.paddle_left.rect.y = max(self.paddle_left.rect.y, 0)
        self.paddle_left.rect.y = min(self.paddle_left.rect.y, self.screen_height - self.paddle_left.height)
