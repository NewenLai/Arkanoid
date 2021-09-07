import pygame as pg
from Arkanoid import ancho, alto
from Arkanoid.escenas import Portada, Partida, Records

pg.init()

class Game():
    def __init__(self):
        pantalla = pg.display.set_mode((alto, ancho))
        self.escenas = [Portada(pantalla), Partida(pantalla), Records(pantalla)]
    
    def start(self):
        
        i = 0
        while True:
            self.escenas[i].bucle_ppal()
            i +=1
            if i == len(self.escenas):
                i = 0
            # formula matematica equivalente al if de arriba
            # i = (i+1) % len(self.escenas)
