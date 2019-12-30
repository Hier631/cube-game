import random
import pygame

from Utils import load_image
from Globals import WIDTH, HEIGHT

class Entity(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image, True)
        self.image_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.centerx = random.randint(0, WIDTH)
        self.speed = 0.2

    def MoveVertically(self, time):
        self.rect.centery += self.speed * time

    def CheckVerticalLimits(self):
        if self.rect.top >=  HEIGHT:
            self.rect.top = 0
            self.rect.centerx = random.randint(0, WIDTH)

    def CheckHorizontalLimits(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = 0
