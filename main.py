import pygame
import random

# Inicialización de PyGame
pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Crear la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Nave Espacial")

# Crear imágenes predeterminadas
player_image = pygame.Surface((50, 30))
player_image.fill(WHITE)
pygame.draw.polygon(player_image, RED, [(0, 30), (25, 0), (50, 30)])

asteroid_image = pygame.Surface((40, 40))
asteroid_image.fill(BLACK)
pygame.draw.circle(asteroid_image, WHITE, (20, 20), 20)

# Función para dibujar el jugador
def draw_player(x, y):
    screen.blit(player_image, (x, y))

# Clase para los asteroides
class Asteroid:
    def _init_(self):
        self.x = random.randint(0, SCREEN_WIDTH - asteroid_image.get_width())
        self.y = random.randint(-100, -40)
        self.speed = random.randint(4, 8)
    
    def update(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = random.randint(-100, -40)
            self.x = random.randint(0, SCREEN_WIDTH - asteroid_image.get_width())
            self.speed = random.randint(4, 8)
    
    def draw(self):
        screen.blit(asteroid_image, (self.x, self.y))

# Función principal del juego
def game():
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT - 100
    player_speed = 5

    asteroids = [Asteroid() for _ in range(5)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_image.get_width():
            player_x += player_speed
        
        screen.fill(BLACK)
        
        draw_player(player_x, player_y)

        for asteroid in asteroids:
            try:
                asteroid.update()
                asteroid.draw()
            except Exception as e:
                print(f"Error actualizando el asteroide: {e}")
        
        pygame.display.flip()
        pygame.time.Clock().tick(60)
    
    pygame.quit()

# Función para mostrar el menú principal
def main_menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
        
        screen.fill(BLACK)
        font = pygame.font.Font(None, 74)
        text = font.render("Presiona ESPACIO para jugar", True, WHITE)
        screen.blit(text, (50, SCREEN_HEIGHT // 2 - 50))
        
        pygame.display.flip()

    pygame.quit()

# Iniciar el juego
_name_ = "_main_"
if _name_ == "_main_":
    main_menu()