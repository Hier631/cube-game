import pygame
from pygame.locals import *

from Globals import WIDTH, HEIGHT

def load_image(filename, transparent=False):
    try: image= pygame.image.load(filename)
    except pygame.error as message:
        raise SystemExit(message)
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