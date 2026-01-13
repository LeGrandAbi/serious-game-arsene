import pygame as pg

from settings import *
from inputs import Inputs
from data import Data
from game import Game

pg.init()

display = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
inputs = Inputs()
data = Data()

game = Game(display, clock, inputs, data)
game.run()
