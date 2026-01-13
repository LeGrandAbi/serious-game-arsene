import pygame as pg
from sys import exit

from settings import *

class Screen:
	def __init__(self, display, clock, inputs, data):
		self.display = display
		self.clock = clock
		self.inputs = inputs
		self.data = data

	def run(self):
		self.inputs.update()
		while not (self.inputs.quit or self.exit_condition()):
			self.inputs.update()
			self.update()
			self.display.fill((0,0,0))
			self.draw_display()
			pg.display.flip()
			self.clock.tick(MAX_FPS)
		if self.inputs.quit:
			pg.quit()
			exit()

	def draw_display(self):
		self.display.fill((0, 0, 0))
		pg.display.flip()

	def update(self):
		pass

	def exit_condition(self):
		return False


class GameOverScreen(Screen):
	def __init__(self, display, clock, inputs, data):
		super().__init__(display, clock, inputs, data)
		self.next = False

	def draw_display(self):
		pg.draw.circle(self.display, (255, 0, 0), (400,400), 64)

	def exit_condition(self):
		return self.inputs.keys["primary"].keydown


class StartingScreen(Screen):
	def __init__(self, display, clock, inputs, data):
		super().__init__(display, clock, inputs, data)

	def draw_display(self):
		pg.draw.circle(self.display, (0, 255, 0), (400,400), 128)

	def exit_condition(self):
		return self.inputs.keys["primary"].keydown


if __name__ == "__main__":
	import main