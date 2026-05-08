import pygame
import sys

# Window setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Engine v0.0001")
clock = pygame.time.Clock()

# Ball properties
x, y = 400, 50
vx, vy = 3, 0
radius = 20
gravity = 0.5
damping = 0.8

#Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #Physics
    vy += gravity
    x += vx
    y += vy

    # Bounce off walls
    if x + radius > WIDTH or x - radius < 0:
        vx *= -1
    if y + radius > HEIGHT:
        y = HEIGHT - radius
        vy *= -damping

    # Draw
    screen.fill((15, 15, 15))
    pygame.draw.circle(screen, (255, 80, 80), (int(x), int(y)), radius)
    pygame.display.flip()
    clock.tick(60)