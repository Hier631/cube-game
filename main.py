#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame, random
from pygame.locals import *
 
# Constantes
WIDTH = 640
HEIGHT = 480
 
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

class Sword(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('images/sword.png', True)
        self.image_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.centerx = random.randint(0, WIDTH)
        self.speed = 0.2

    def actualizar(self, time, vidas, sprite, *osprite):
        self.rect.centery += self.speed * time
        if self.rect.top >=  HEIGHT:
            self.rect.top = 0
            self.rect.centerx = random.randint(0, WIDTH)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = 0

        if collision_detection(self, sprite):
                vidas -= 1
                if vidas > 0:
                    self.rect.top = 0
                    self.rect.centerx = random.randint(0, WIDTH)

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
            
        return vidas

class Cube(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('images/cube.png', True)
        self.image_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.centerx = random.randint(0, WIDTH)
        self.speed = 0.2

    def actualizar(self, time, vidas, sprite, *osprite):
        self.rect.centery += self.speed * time
        if self.rect.top >=  HEIGHT:
            self.rect.top = 0
            self.rect.centerx = random.randint(0, WIDTH)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = 0

        if collision_detection(self, sprite):
            vidas -= 1
            if vidas > 0:
                self.rect.top = 0
                self.rect.centerx = random.randint(0, WIDTH)

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
            
        return vidas

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('images/apple.png', True)
        self.image_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.centerx = random.randint(0, WIDTH)
        self.speed = 0.2

    def actualizar(self, time, puntos, sprite, *osprite):
        self.rect.centery += self.speed * time
        if self.rect.top >=  HEIGHT:
            self.rect.top = 0
            self.rect.centerx = random.randint(0, WIDTH)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = 0

        if collision_detection(self, sprite):
            puntos += 100
            self.rect.top = 0
            self.rect.centerx = random.randint(0, WIDTH)

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

        return puntos

class Orange(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('images/orange.png', True)
        self.image_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.centerx = random.randint(0, WIDTH)
        self.speed = 0.2

    def actualizar(self, time, puntos, sprite, *osprite):
        self.rect.centery += self.speed * time
        if self.rect.top >=  HEIGHT:
            self.rect.top = 0
            self.rect.centerx = random.randint(0, WIDTH)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = 0

        if collision_detection(self, sprite):
            puntos += 50
            self.rect.top = 0
            self.rect.centerx = random.randint(0, WIDTH)

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
            
        return puntos

class Watermelon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('images/watermelon.png', True)
        self.image_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.centerx = random.randint(0, WIDTH)
        self.speed = 0.2

    def actualizar(self, time, puntos, sprite, *osprite):
        self.rect.centery += self.speed * time
        if self.rect.top >=  HEIGHT:
            self.rect.top = 0
            self.rect.centerx = random.randint(0, WIDTH)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = 0

        if collision_detection(self, sprite):
            puntos += 150
            self.rect.top = 0
            self.rect.centerx = random.randint(0, WIDTH)

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
            
        return puntos

class Vida(pygame.sprite.Sprite):
    def __init__(self, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('images/heart.png', True)
        self.image_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery

# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------

def load_image(filename, transparent=False):
    try: image= pygame.image.load(filename)
    except pygame.error, message:
        raise SystemExit, message
    image = image.convert()
    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)
    return image

def collision_detection(sprite1, sprite2):
    offset_x, offset_y = (sprite2.rect.left - sprite1.rect.left), (sprite2.rect.top - sprite1.rect.top)
    if (sprite1.image_mask.overlap(sprite2.image_mask, (offset_x, offset_y)) != None):
        return True

def texto(texto, posx, posy, color=(0, 0, 0), size = 20):
    fuente = pygame.font.Font('fonts/Unique.ttf', size)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect

# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Hier631')

    background_image = load_image('images/background.png')
    player = Player()
    sword1= Sword()
    orange1 = Orange()
    apple1 = Apple()
    watermelon1 = Watermelon()
    cube1 = Cube()
    vida1 = Vida(15, 10)
    vida2 = Vida(35, 10)
    vida3 = Vida(55, 10)

    clock = pygame.time.Clock()

    cube = []
    sword = []

    puntos = 0
    vidas = 3
    count1 = 1000.0
    count2 = 0
    
    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

        for index in range(0, 1000):
            if puntos >= count1 and index == count1/1000 and count2 == 0:
                if len(cube) <= 4:
                    cube.append(Cube())
                count1 += 1000
                count2 = 1

        for index in range(0, 1000):
            if puntos >= count1 and index == count1/1000 and count2 == 1:
                if len(sword) <=4:
                    sword.append(Sword())
                count1 += 1000
                count2 = 0

        for index in range(0, len(cube)):
            cube[index].speed = count1 / 100000 + 0.2

        for index in range(0, len(sword)):
            sword[index].speed = count1 / 100000 + 0.2
            
        cube1.speed = count1 / 100000 + 0.2
        sword1.speed = count1 / 100000 + 0.2
        orange1.speed = count1 / 100000 + 0.2
        apple1.speed = count1 / 100000 + 0.2
        watermelon1.speed = count1 / 100000 + 0.2

        if vidas > 0:
            player.mover(time, keys)
            for index in range(0, len(cube)):
                vidas = cube[index].actualizar(time, vidas, player, sword1, orange1, apple1, watermelon1, cube1, cube, sword)
            for index in range(0, len(sword)):
                vidas = sword[index].actualizar(time, vidas, player, sword1, orange1, apple1, watermelon1, cube1, cube, sword)
            vidas = sword1.actualizar(time, vidas, player, cube, sword, orange1, apple1, watermelon1, cube1)
            puntos = orange1.actualizar(time, puntos, player, cube, sword, sword1, apple1, watermelon1, cube1)
            puntos = apple1.actualizar(time, puntos, player, cube, sword, sword1, orange1, watermelon1, cube1)
            puntos = watermelon1.actualizar(time, puntos, player, cube, sword, sword1, orange1, apple1, cube1)
            vidas = cube1.actualizar(time, vidas, player, cube, sword, sword1, orange1, apple1, watermelon1)
            
        p_jug, p_jug_rect = texto(str(puntos), WIDTH / 2, 10, size=20)
        game_over, game_over_rect = texto('Game Over', WIDTH / 2, HEIGHT / 2, size=50)
        press_enter, press_enter_rect = texto('Press enter to restart', WIDTH / 2, HEIGHT * 0.60, size=15)
        level_text, level_text_rect = texto('Level: '+str(int(count1)/1000), WIDTH * 0.75, 10, size = 20)
        
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
