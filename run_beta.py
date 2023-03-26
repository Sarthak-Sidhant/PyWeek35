import pygame
import random
import time

# initialize pygame
pygame.init()

# set up the display window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# set up the game clock
clock = pygame.time.Clock()

# set up the font
font = pygame.font.SysFont(None, 48)

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# set up the game variables
player_size = 20
player_x = WINDOW_WIDTH // 2 - player_size // 2
player_y = WINDOW_HEIGHT // 2 - player_size // 2
player_speed = 5

guard_size = 20
guard_x = random.randint(0, WINDOW_WIDTH - guard_size)
guard_y = random.randint(0, WINDOW_HEIGHT - guard_size)
guard_speed = 3

# set up the game loop
game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - player_size:
        player_x += player_speed
    elif keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    elif keys[pygame.K_DOWN] and player_y < WINDOW_HEIGHT - player_size:
        player_y += player_speed

    # move the guard
    guard_x += guard_speed
    if guard_x < 0 or guard_x > WINDOW_WIDTH - guard_size:
        guard_speed *= -1
    guard_y += guard_speed
    if guard_y < 0 or guard_y > WINDOW_HEIGHT - guard_size:
        guard_speed *= -1

    # check for collision between player and guard
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    guard_rect = pygame.Rect(guard_x, guard_y, guard_size, guard_size)
    if player_rect.colliderect(guard_rect):
        game_over = True

    # draw the game elements
    game_window.fill(BLUE)
    pygame.draw.rect(game_window, WHITE, (0, 0, WINDOW_WIDTH, 5))
    pygame.draw.rect(game_window, WHITE, (0, 0, 5, WINDOW_HEIGHT))
    pygame.draw.rect(game_window, WHITE, (WINDOW_WIDTH-5, 0, 5, WINDOW_HEIGHT))
    pygame.draw.rect(game_window, WHITE, (0, WINDOW_HEIGHT-5, WINDOW_WIDTH, 5))
    pygame.draw.circle(game_window, RED, (player_x + player_size//2, player_y + player_size//2), player_size//2)
    pygame.draw.circle(game_window, GREEN, (guard_x + guard_size//2, guard_y + guard_size//2), guard_size//2)

    # update the display
    pygame.display.update()

# draw "game over" message
game_over_message = font.render("Game Over", True, WHITE)
game_window.blit(game_over_message, (WINDOW_WIDTH//2 - game_over_message.get_width()//2,
                                     WINDOW_HEIGHT//2 - game_over_message.get_height()//2))

# draw restart message
restart_message = font.render("Press space to restart", True, WHITE)
game_window.blit(restart_message, (WINDOW_WIDTH//2 - restart_message.get_width()//2,
                                   WINDOW_HEIGHT//2 + game_over_message.get_height()))

pygame.display.update()

# wait for player to press space to restart
restart = False
while not restart:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                restart = True

# reset player and guard positions
player = Player(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
player.x = WINDOW_WIDTH // 2
player.y = WINDOW_HEIGHT // 2
guard.x = random.randint(0, WINDOW_WIDTH - guard_size)
guard.y = random.randint(0, WINDOW_HEIGHT - guard_size)

# reset game variables
game_over = False
score = 0
