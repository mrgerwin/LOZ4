import pygame
import random
class Ball:
    def __init__(self, surface):
        self.surface = surface
        self.x = 500
        self.y = 500
        self.velx = random.randint(-3, 3)
        self.vely = random.randint(-3, 3)
        self.rect = pygame.draw.circle(surface, red, [self.x, self.y], 20)
    def move(self):
        if self.x>= self.surface.get_width() or self.x<= 0:
            self.velx = -self.velx
        if self.y>=self.surface.get_height() or self.y<=0:
            self.vely = -self.vely
        self.rect=self.rect.move(self.velx, self.vely)
        self.x = self.rect.x
        self.y = self.rect.y
        pygame.draw.circle(self.surface, red, [self.rect.x, self.rect.y], 20)
red = (255, 0, 0)
white = (255, 255, 255)
Window = pygame.display.set_mode([1000, 600])
clock = pygame.time.Clock()
ball_list = []
for ball in range(5):
    ball_list.append(Ball(Window))
while True:
    pygame.Surface.fill(Window, white)
    for ball in ball_list:
        ball.move()
    pygame.display.flip()
    clock.tick(30)
