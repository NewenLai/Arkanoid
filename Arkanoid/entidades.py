from pygame import sprite
import pygame as pg
from pygame.sprite import Sprite
from .import alto, ancho

class Raqueta (Sprite):
    disfraz = "electric00.png"
    def __init__(self, **kwargs):
        self.image = pg.image.load(f"resources/images/{self.disfraz}" )#print("cadena{}".format(variable)) -> print(f"cadena{variable}")
        self.rect = self.image.get_rect(**kwargs)

    def update(self):
        if pg.key.get_pressed()[pg.K_LEFT]:
            self.rect.x -= 5
        if self.rect.left <= 0:
            self.rect.left = 0
        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.rect.x += 5
        if self.rect.right >= alto:
            self.rect.right= alto

class Bola(Sprite):
    disfraz = "ball1.png"
    def __init__(self, **kwargs):
        self.image = pg.image.load(f"resources/images/{self.disfraz}")
        self.rect = self.image.get_rect(**kwargs)
        self.v_x = 5
        self.v_y = 5
        self.viva = True 
        self.posicion = kwargs

    def update(self):
        self.rect.x += self.v_x
        if self.rect.x <=0 or self.rect.right >= alto:
            self.v_x *= -1
        self.rect.y += self.v_y
        if self.rect.y <=0 :
            self.v_y *= -1
        if self.rect.bottom >= ancho:
            self.viva =  False
            self.rect = self.image.get_rect(**self.posicion)
    
    def colision(self, otro):
        if self.rect.right >= otro.rect.left and self.rect.left <= otro.rect.right and self.rect.bottom >= otro.rect.top and self.rect.top <= otro.rect.bottom:
            self.v_y *= -1