import pygame

class Paddle:
    def __init__(self, x, y, up_key, down_key):
        # Inicializa os atributos da raquete
        self.x = x
        self.y = y
        self.width = 20  # Largura da raquete
        self.height = 100  # Altura da raquete
        self.color = (255, 255, 255)  # Cor da raquete (branco)
        self.speed = 5  # Velocidade de movimento da raquete
        # Cria um retângulo para a raquete com base nos atributos
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.up_key = up_key  # Tecla para mover a raquete para cima
        self.down_key = down_key  # Tecla para mover a raquete para baixo

    def move(self, screen_height):
        # Obtém as teclas pressionadas no momento
        keys = pygame.key.get_pressed()
        # Move a raquete para cima se a tecla correspondente for pressionada e a raquete não alcançou o topo da tela
        if keys[self.up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        # Move a raquete para baixo se a tecla correspondente for pressionada e a raquete não alcançou a parte inferior da tela
        if keys[self.down_key] and self.rect.bottom < screen_height:
            self.rect.y += self.speed

    def draw(self, screen):
        # Desenha a raquete na tela
        pygame.draw.rect(screen, self.color, self.rect)

class Ball:
    def __init__(self, x, y):
        # Inicializa os atributos da bola
        self.x = x
        self.y = y
        self.radius = 10  # Raio da bola
        self.color = (255, 0, 0)  # Cor da bola (vermelho)
        self.speed_x = 3  # Velocidade horizontal da bola
        self.speed_y = 3  # Velocidade vertical da bola
        # Cria um retângulo para a bola com base nos atributos
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)

    def move(self):
        # Move a bola na direção especificada pelas velocidades x e y
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Inverte a direção horizontal se a bola atingir as bordas laterais da tela
        if self.rect.left <= 0 or self.rect.right >= pygame.display.get_surface().get_width():
            self.speed_x *= -1
        # Inverte a direção vertical se a bola atingir as bordas superior ou inferior da tela
        if self.rect.top <= 0 or self.rect.bottom >= pygame.display.get_surface().get_height():
            self.speed_y *= -1

    def check_collision(self, paddle):
        # Verifica se houve colisão entre a bola e a raquete
        if self.rect.colliderect(paddle.rect):
            self.speed_y *= -1  # Inverte a direção vertical da bola

    def draw(self, screen):
        # Desenha a bola na tela
        pygame.draw.ellipse(screen, self.color, self.rect)
