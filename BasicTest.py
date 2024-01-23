import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
GRAVITY = 0.5
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Ball")

ball_color = WHITE
ball_position = [WIDTH // 2, HEIGHT // 2]
ball_velocity = [0, 0]

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update ball position
    ball_velocity[1] += GRAVITY
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]

    # Bounce off the ground
    if ball_position[1] + BALL_RADIUS > HEIGHT:
        ball_velocity[1] *= -0.8  # Reverse direction and lose some energy
        ball_position[1] = HEIGHT - BALL_RADIUS

    # Draw background
    screen.fill(BLACK)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (int(ball_position[0]), int(ball_position[1])), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    clock.tick(FPS)
