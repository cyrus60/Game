import pygame, sys
from pygame.locals import *
import random

black = 0, 0, 0
purple = 200, 0, 250

# Defines ball object          
class Ball():
    def __init__(self):
        self.x = 250
        self.y = 250
        self.speed = 20
        self.acceleration = 5
        self.rect = ''

    def draw(self):
        self.ball = pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), 32)
        self.rect = pygame.rect.Rect(self.ball)

    def right(self):
        self.x = self.x+25
        if self.x > 500:
            self.x = 0

    def left(self):
        self.x = self.x-25
        if self.x < 0:
            self.x = 500

    def bounce(self, key):
        if self.y > 459:
            self.speed -= self.acceleration
            self.speed = - self.speed
        elif self.y <= 459:
            self.acceleration = 5
            self.speed += self.acceleration
            if key[pygame.K_SPACE]:
                self.acceleration = self.acceleration * 2
                self.speed += self.acceleration
        
        self.y += self.speed
            

# Defines star object
class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randrange(30, 470)
        self.y = random.randrange(50, 435)
        self.image = ''
        self.rect = ''

    def draw(self, rect):
        image = pygame.image.load('img/star.png').convert_alpha()
        self.image = pygame.transform.scale(image, (image.get_width() * .8, image.get_height() * .8))
        self.rect = image.get_rect()
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.rect)
        if rect.colliderect(self.rect):
            self.rect.center = (-100, -100)
            screen.blit(self.image, self.rect)
            self.x, self.y = random.randrange(1, 499), random.randrange(20, 435)
            self.rect.center = (self.x, self.y)
            screen.blit(self.image, self.rect)


def main():
    ball = Ball()
    star = Star() 

    # Main game loop
    while True: 
        pygame.time.delay(70)

        # Events
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            ball.left()

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            ball.right()

        # Game Logic
        screen.fill(purple)
        ball.draw()
        ball.bounce(keys)
        ballRect = ball.rect
        star.draw(ballRect)
        
        pygame.draw.rect(screen, (0, 0, 0), (0, 460, 500, 100))
        pygame.display.update()


if __name__ == '__main__':
    size = width, height = 500, 500
    pygame.init
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("BallGame v 1.0")
    main()