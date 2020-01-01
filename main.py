#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame, random

from pygame.locals import *
from Utils import load_image
from Utils import texto
from Globals import WIDTH
from Globals import HEIGHT
from Evil import Evil
from Good import Good
 
LEVEL_MAX_POINTS = 1000
 
swordImage = "images/sword.png"
cubeImage = "images/cube.png"
appleImage = "images/apple.png"
orangeImage = "images/orange.png"
watermelonImage = "images/watermelon.png"
    
applePoints = 100
orangePoints = 50
watermelonPoints = 150
 
# Clases
# ---------------------------------------------------------------------

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('images/player.png', True)
        self.image_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT
        self.speed = 0.5

    def mover(self, time, keys):
        if self.rect.left >= 0:
            if keys[K_LEFT]:
                self.rect.centerx -= self.speed * time
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right <= WIDTH:
            if keys[K_RIGHT]:
                self.rect.centerx += self.speed * time
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Vida(pygame.sprite.Sprite):
    def __init__(self, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('images/heart.png', True)
        self.image_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery

# ---------------------------------------------------------------------
 
#Increase the level and add new enemies
def increaseLevel(points, level, cubeList, swordList):
    if points >= level * LEVEL_MAX_POINTS:
        if len(swordList) < 5:
            if level % 2 == 1:
                cubeList.append(Evil(cubeImage))
            else:
                swordList.append(Evil(swordImage))            
        level += 1
        
    return level
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Hier631')

    background_image = load_image('images/background.png')
    player = Player()
    sword1= Evil(swordImage)
    orange1 = Good(orangeImage, orangePoints)
    apple1 = Good(appleImage, applePoints)
    watermelon1 = Good(watermelonImage, watermelonPoints)
    cube1 = Evil(cubeImage)
    vida1 = Vida(15, 10)
    vida2 = Vida(35, 10)
    vida3 = Vida(55, 10)

    clock = pygame.time.Clock()

    cube = []
    sword = []

    puntos = 0
    vidas = 3
    level = 1
    
    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

        level = increaseLevel(puntos, level, cube, sword)

        for index in range(0, len(cube)):
            cube[index].speed = level / 100 + 0.2

        for index in range(0, len(sword)):
            sword[index].speed = level / 100 + 0.2
            
        cube1.speed = level / 100 + 0.2
        sword1.speed = level / 100 + 0.2
        orange1.speed = level / 100 + 0.2
        apple1.speed = level / 100 + 0.2
        watermelon1.speed = level / 100 + 0.2

        if vidas > 0:
            player.mover(time, keys)
            for index in range(0, len(cube)):
                vidas = cube[index].Update(time, vidas, player, sword1, orange1, apple1, watermelon1, cube1, cube, sword)
            for index in range(0, len(sword)):
                vidas = sword[index].Update(time, vidas, player, sword1, orange1, apple1, watermelon1, cube1, cube, sword)
            vidas = sword1.Update(time, vidas, player, cube, sword, orange1, apple1, watermelon1, cube1)
            puntos = orange1.Update(time, puntos, player, cube, sword, sword1, apple1, watermelon1, cube1)
            puntos = apple1.Update(time, puntos, player, cube, sword, sword1, orange1, watermelon1, cube1)
            puntos = watermelon1.Update(time, puntos, player, cube, sword, sword1, orange1, apple1, cube1)
            vidas = cube1.Update(time, vidas, player, cube, sword, sword1, orange1, apple1, watermelon1)
            
        p_jug, p_jug_rect = texto(str(puntos), WIDTH / 2, 10, size=20)
        game_over, game_over_rect = texto('Game Over', WIDTH / 2, HEIGHT / 2, size=50)
        press_enter, press_enter_rect = texto('Press enter to restart', WIDTH / 2, HEIGHT * 0.60, size=15)
        level_text, level_text_rect = texto('Level: '+str(level), WIDTH * 0.75, 10, size = 20)
        
        screen.blit(background_image, (0, 0))
        screen.blit(sword1.image, sword1.rect)
        screen.blit(orange1.image, orange1.rect)
        screen.blit(apple1.image, apple1.rect)
        screen.blit(watermelon1.image, watermelon1.rect)
        for index in range(0, len(cube)):
            screen.blit(cube[index].image, cube[index].rect)
        for index in range(0, len(sword)):
            screen.blit(sword[index].image, sword[index].rect)
        screen.blit(cube1.image, cube1.rect)
        screen.blit(player.image, player.rect)
        screen.blit(p_jug, p_jug_rect)
        screen.blit(level_text, level_text_rect)
        if vidas >= 1:
            screen.blit(vida1.image, vida1.rect)
        if vidas >= 2:
            screen.blit(vida2.image, vida2.rect)
        if vidas == 3:
            screen.blit(vida3.image, vida3.rect)
        if vidas <= 0:
            screen.blit(game_over, game_over_rect)
            screen.blit(press_enter, press_enter_rect)
            if keys[K_RETURN]:
                main()
                
        pygame.display.flip()

    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()
