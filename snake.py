import pygame
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
CELL_SIZE = 20
FPS = 10

DIRECTIONS = [[CELL_SIZE, 0], [-CELL_SIZE, 0], [0, CELL_SIZE], [0, -CELL_SIZE]]

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
font = pygame.font.SysFont('Arial', 25)
score = 0 

# Initialize snake and food
snake = [[random.randint(1, WIDTH//CELL_SIZE - 2) * CELL_SIZE, 
          random.randint(1, HEIGHT//CELL_SIZE - 2) * CELL_SIZE]]
# start_x = WIDTH // 2 // CELL_SIZE * CELL_SIZE
# start_y = HEIGHT // 2 // CELL_SIZE * CELL_SIZE
# snake = [(start_x, start_y)]
direction = random.choice(DIRECTIONS)
food = [random.randint(1, WIDTH//CELL_SIZE - 2) * CELL_SIZE, 
        random.randint(1, HEIGHT//CELL_SIZE - 2) * CELL_SIZE]

## Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Draw food
    pygame.draw.circle(screen, WHITE, (food[0], food[1]), CELL_SIZE//2, 0)
    
    # Draw snake
    for segment in snake:
        cx = segment[0] + CELL_SIZE // 2
        cy = segment[1] + CELL_SIZE // 2
        pygame.draw.circle(screen, YELLOW, (cx, cy), CELL_SIZE // 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    elif keys[pygame.K_UP] and direction != [0, CELL_SIZE]:
        direction = [0, -CELL_SIZE]
    elif keys[pygame.K_DOWN] and direction != [0, -CELL_SIZE]:
        direction = [0, CELL_SIZE]
    elif keys[pygame.K_LEFT] and direction != [CELL_SIZE, 0]:
        direction = [-CELL_SIZE, 0]
    elif keys[pygame.K_RIGHT] and direction != [-CELL_SIZE, 0]:
        direction = [CELL_SIZE, 0]
    
    head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
    snake.insert(0, head)
    if food in snake[1:]:
        food = [random.randint(0, WIDTH//CELL_SIZE - 1) * CELL_SIZE, 
                random.randint(0, HEIGHT//CELL_SIZE - 1) * CELL_SIZE]
    elif head == food:
        score += 1
        food = [random.randint(0, WIDTH//CELL_SIZE - 1) * CELL_SIZE, 
        random.randint(0, HEIGHT//CELL_SIZE - 1) * CELL_SIZE]
    else:
        snake.pop()

    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or \
    head in snake[1:]:
        running = False
    
    score_surface = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_surface, (10, 10))

    pygame.display.update()

pygame.quit()