import pygame
import random
pygame.init()
# Configuración de la ventana del juego
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Barra del jugador
PLAYER_WIDTH, PLAYER_HEIGHT = 15, 100
player = pygame.Rect(50, HEIGHT // 2 - PLAYER_HEIGHT // 2, PLAYER_WIDTH, PLAYER_HEIGHT)

# Barra del oponente
opponent = pygame.Rect(WIDTH - 50 - PLAYER_WIDTH, HEIGHT // 2 - PLAYER_HEIGHT // 2, PLAYER_WIDTH, PLAYER_HEIGHT)

# Bola
BALL_SIZE = 20
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

# Velocidad de las barras
PLAYER_SPEED = 10
OPPONENT_SPEED = 8

# Marcadores
player_score = 0
opponent_score = 0
font = pygame.font.SysFont(None, 50)

def draw_window():
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, player)
    pygame.draw.rect(WIN, WHITE, opponent)
    pygame.draw.ellipse(WIN, WHITE, ball)
    player_score_display = font.render(str(player_score), True, WHITE)
    opponent_score_display = font.render(str(opponent_score), True, WHITE)
    WIN.blit(player_score_display, (WIDTH // 4, 30))
    WIN.blit(opponent_score_display, (WIDTH * 3 // 4 - opponent_score_display.get_width(), 30))
    pygame.display.update()

def move_player(keys_pressed):
    if keys_pressed[pygame.K_w] and player.top > 0:
        player.y -= PLAYER_SPEED
    if keys_pressed[pygame.K_s] and player.bottom < HEIGHT:
        player.y += PLAYER_SPEED

def move_opponent():
    if opponent.centery < ball.centery:
        opponent.y += OPPONENT_SPEED
    if opponent.centery > ball.centery:
        opponent.y -= OPPONENT_SPEED

def move_ball():
    global ball_speed_x, ball_speed_y, player_score, opponent_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Rebotar la bola en los bordes
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Rebotar la bola en las barras
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Marcar puntos y restablecer la posición de la bola
    if ball.left <= 0:
        opponent_score += 1
        reset_ball()
    if ball.right >= WIDTH:
        player_score += 1
        reset_ball()

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        move_player(keys_pressed)
        move_opponent()
        move_ball()
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()
