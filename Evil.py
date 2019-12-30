import random

from Entity import Entity
from Utils import collision_detection
from Globals import WIDTH, HEIGHT

class Evil(Entity):

    def __init__(self, image):
        Entity.__init__(self, image)

    def subtractLives(self, vidas, sprite):
        if collision_detection(self, sprite):
            vidas -= 1
            if vidas > 0:
                self.rect.top = 0
                self.rect.centerx = random.randint(0, WIDTH)
        return vidas

    def CheckCollision(self, *osprite):
        for elemento in osprite:
            if type(elemento) == list:
                for x in elemento:
                    if x != self:
                        if collision_detection(self, x):
                            self.rect.top = 0
                            self.rect.centerx = random.randint(0, WIDTH)
            else:
                if collision_detection(self, elemento):
                    self.rect.top = 0
                    self.rect.centerx = random.randint(0, WIDTH)

    def Update(self, time, vidas, sprite, *osprite):
        self.MoveVertically(time)
        self.CheckVerticalLimits()
        self.CheckHorizontalLimits()
        vidas = self.subtractLives(vidas, sprite)
        self.CheckCollision(*osprite)

        return vidas
