import pygame as pg

from settings import *
from inputs import Inputs
from data import Data
from screen import GameOverScreen, StartingScreen
from game import Game

pg.init()

display = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
inputs = Inputs()
data = Data()

while True:
	starting_screen = StartingScreen(display, clock, inputs, data)
	starting_screen.run()
	game = Game(display, clock, inputs, data)
	game.run()
	gameover_screen = GameOverScreen(display, clock, inputs, data)
	gameover_screen.run()