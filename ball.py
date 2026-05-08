import pygame
import sys

class Ball:
    def __init__(self, x, y, vx, vy, radius):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
    def update(self):
        self.vy += gravity
        self.x += self.vx
        self.y += self.vy

        if self.x + self.radius >= WIDTH or self.x - self.radius <= 0:
            self.vx *= -1
        if self.y + self.radius >= HEIGHT:
            self.y = HEIGHT - self.radius
            self.vy *= -damping
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 80, 80), (int(self.x), int(self.y)), self.radius)
    def collides_with(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx**2 +dy**2) ** 0.5
        return distance < self.radius + other.radius

# Window setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Engine v0.0001")
clock = pygame.time.Clock()

# Ball properties
balls = [
    Ball(400, 50, 3, 0, 20),
    Ball(200, 100, -2, 1, 15)
]
gravity = 0.5
damping = 0.8

#Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #Physics
    screen.fill((15, 15, 15))
    for ball in balls:
        ball.update()
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                if balls[i].collides_with(balls[j]):
                    balls[i].vx *= -1
                    balls[i].vy *= -1
                    balls[j].vx *= -1
                    balls[j].vy *= -1
        ball.draw(screen)
    pygame.display.flip()
    clock.tick(60)