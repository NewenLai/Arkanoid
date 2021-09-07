import pygame as pg
from pygame.constants import KEYDOWN
from . import FPS, alto, ancho
from .entidades import Raqueta, Bola

class Escena():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_ppal(self):
        pass

class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.logo = pg.image.load("resources/images/arkanoid_name.png")
        fuente = pg.font.Font("resources/fonts/LibreFranklin-VariableFont_wght.ttf", 45)
        self.Texto = fuente.render("Pulsa <SPC> para comenzar", True, (0,0,0))
        self.anchoTexto = self.Texto.get_width()

    def bucle_ppal(self):
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        game_over = True

            self.pantalla.fill ((80, 80, 255))
            self.pantalla.blit(self.logo, (140, 140))
            self.pantalla.blit(self.Texto, ((alto - self.anchoTexto)//2, 640))
            pg.display.flip()

class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.fondo = pg.image.load("resources/images/background.jpg")
        self.player = Raqueta(midbottom= (alto//2, ancho - 15))
        self.bola =  Bola(center = (alto//2, ancho//2))
        self.vidas = 3

    def bucle_ppal(self):
        self.vidas = 3
        while self.vidas > 0:
            self.reloj.tick(FPS)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()
            self.player.update()
            self.bola.update()
            self.bola.colision(self.player)

            if not self.bola.viva:
                self.vidas -= 1
                self.bola.viva = True

            self.pantalla.blit(self.fondo, (0, 0))
            self.pantalla.blit(self.player.image, self.player.rect)
            self.pantalla.blit(self.bola.image, self.bola.rect)

            pg.display.flip()

class Records(Escena):
    pass