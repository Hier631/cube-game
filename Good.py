import random

from Entity import Entity
from Utils import collision_detection
from Globals import WIDTH, HEIGHT

class Good(Entity):

    def __init__(self, image, points):
        Entity.__init__(self, image)
        self.points = points

    def addPoints(self, points, sprite):
        if collision_detection(self, sprite):
            points += self.points
            self.rect.top = 0
            self.rect.centerx = random.randint(0, WIDTH)
        return points

    def CheckCollision(self, *osprite):
        for elemento in osprite:
            if type(elemento) == list:
                for x in elemento:
                    if collision_detection(self, x):
                        self.rect.top = 0
                        self.rect.centerx = random.randint(0, WIDTH)
            else:
                if collision_detection(self, elemento):
                    self.rect.top = 0
                    self.rect.centerx = random.randint(0, WIDTH)

    def Update(self, time, puntos, sprite, *osprite):
        self.MoveVertically(time)
        self.CheckVerticalLimits()
        self.CheckHorizontalLimits()
        puntos = self.addPoints(puntos, sprite)
        self.CheckCollision(*osprite)

        return puntos
