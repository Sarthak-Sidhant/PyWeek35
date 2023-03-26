import pygame
import random
import time

# initialize pygame
pygame.init()

# set up the window display
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Stealth Game")

# set up the game clock
clock = pygame.time.Clock()

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# define the player
player_size = 25
player_pos = [WINDOW_WIDTH//2, WINDOW_HEIGHT//2]

# define the guard
guard_size = 25
guard_pos = [random.randint(0, WINDOW_WIDTH-guard_size), random.randint(0, WINDOW_HEIGHT-guard_size)]

# define the boundary
boundary_width = 10
boundary_rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
boundary_rect.inflate_ip(-boundary_width*2, -boundary_width*2)

# define game over variable
game_over = False

# define movement variables
player_speed = 5

# define font
font = pygame.font.Font(None, 36)

def main_loop():
    # game loop
    while not game_over:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > boundary_rect.left:
            player_pos[0] -= player_speed
        elif keys[pygame.K_RIGHT] and player_pos[0] < boundary_rect.right - player_size:
            player_pos[0] += player_speed
        if keys[pygame.K_UP] and player_pos[1] > boundary_rect.top:
            player_pos[1] -= player_speed
        elif keys[pygame.K_DOWN] and player_pos[1] < boundary_rect.bottom - player_size:
            player_pos[1] += player_speed

        # move the guard
        if guard_pos[0] < player_pos[0]:
            guard_pos[0] += 1
        elif guard_pos[0] > player_pos[0]:
            guard_pos[0] -= 1
        if guard_pos[1] < player_pos[1]:
            guard_pos[1] += 1
        elif guard_pos[1] > player_pos[1]:
            guard_pos[1] -= 1

        # check for collision
        if pygame.Rect(player_pos[0], player_pos[1], player_size, player_size).colliderect(
                pygame.Rect(guard_pos[0], guard_pos[1], guard_size, guard_size)):
            game_over = True

        # draw everything
        game_window.fill(BLUE)
        pygame.draw.rect(game_window, WHITE, boundary_rect, boundary_width)
        pygame.draw.circle(game_window, RED, (player_pos[0] + player_size//2, player_pos[1] + player_size//2), player_size//2)
        pygame.draw.circle(game_window, GREEN, (guard_pos[0] + guard_size//2, guard_pos[1] + guard_size//2), guard_size//2)

        # update the display
        pygame.display.update()

        # tick the clock
        clock.tick(60)
main_loop
# draw "game over" message and restart option
restart_screen = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
restart_screen.fill((0, 0, 255))  # fill with blue color
restart_message = font.render("Game Over", True, WHITE)
restart_screen.blit(restart_message, (WINDOW_WIDTH//2 - restart_message.get_width()//2,
                                      WINDOW_HEIGHT//2 - restart_message.get_height()//2))
restart_message = font.render("Press SPACE to Restart", True, WHITE)
restart_screen.blit(restart_message, (WINDOW_WIDTH//2 - restart_message.get_width()//2,
                                      WINDOW_HEIGHT//2 + restart_message.get_height()))
game_window.blit(restart_screen, (0, 0))
pygame.display.update()

# wait for player to press space to restart
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # reset game variables and restart game loop
            player_x = WINDOW_WIDTH // 2
            player_y = WINDOW_HEIGHT // 2
            guard_x = random.randint(0, WINDOW_WIDTH - guard_size)
            guard_y = random.randint(0, WINDOW_HEIGHT - guard_size)
            game_over = False
            main_loop()
    pygame.display.update()
    pygame.time.delay(1000)
