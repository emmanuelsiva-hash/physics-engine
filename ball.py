import random
import pygame
import sys

WIDTH, HEIGHT = 800, 600
gravity = 0.5
damping = 0.8

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
        if self.x + self.radius >= WIDTH:
            self.x = WIDTH - self.radius
            self.vx *= -1
        elif self.x - self.radius <= 0:
            self.x = self.radius
            self.vx *= -1
        if self.y + self.radius >= HEIGHT:
            self.y = HEIGHT - self.radius
            self.vy *= damping
        elif self.y - self.radius <= 0:
            self.y = self.radius
            self.vy *= -1
        if abs()

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 80, 80), (int(self.x), int(self.y)), self.radius)

    def collides_with(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx**2 + dy**2) ** 0.5
        return distance < self.radius + other.radius
    if distance == 0:
        distance = 0.0001

balls = []
for _ in range(35):
    balls.append(Ball(
        random.randint(50, 750),
        random.randint(50, 300),
        random.randint(-4, 4),
        random.randint(-2, 2),
        random.randint(10, 25)
    ))

while True:
    dx = balls[0].x - balls[1].x
    dy = balls[0].y - balls[1].y
    distance = (dx**2 + dy**2) ** 0.5
    if distance > balls[0].radius + balls[1].radius + 10:
        break
    balls[1].x = random.randint(100, 700)
    balls[1].y = random.randint(50, 300)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Engine v0.0001")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((15, 15, 15))

    for ball in balls:
        ball.update()

    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            if balls[i].collides_with(balls[j]):
                dx = balls[i].x - balls[j].x
                dy = balls[i].y - balls[j].y
                distance = (dx**2 + dy**2) ** 0.5
                overlap = (balls[i].radius + balls[j].radius) - distance
                nx = dx / distance
                ny = dy / distance
                balls[i].x += nx * overlap / 2
                balls[i].y += ny * overlap / 2
                balls[j].x -= nx * overlap / 2
                balls[j].y -= ny * overlap / 2
                balls[i].vx, balls[j].vx = balls[j].vx, balls[i].vx
                balls[i].vy, balls[j].vy = balls[j].vy, balls[i].vy

    for ball in balls:
        ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)