import pygame as pg
import random as rand

from settings import *
from robot import Robot
from tilemap import TileMap

class Game:
	def __init__(self, display, clock, inputs, data):
		self.display = display
		self.clock = clock
		self.inputs = inputs
		self.data = data

		self.tilemap = TileMap(TILEMAP_WIDTH, TILEMAP_HEIGHT, self.data)

		self.robots = [Robot(self.data) for _ in range(NB_ROBOTS)]

	def run(self):
		while not self.inputs.quit:
			self.inputs.update()
			self.update_sprites()
			self.update_display()
			self.clock.tick(MAX_FPS)

	def update_display(self):
		self.display.fill((0,0,0))

		# draws the tiles
		for x in range(self.tilemap.width):
			for y in range(self.tilemap.height):
				texture = self.tilemap.get_image(x, y)
				self.display.blit(texture, (x*TILE_SIZE, y*TILE_SIZE))

		# draws the robots
		for robot in sorted(self.robots, key = lambda robot: robot.position.y):
			texture = robot.get_image()
			self.display.blit(texture, texture.get_rect(center=robot.position))

		pg.display.flip()

	def update_sprites(self):
		for robot in self.robots:
			robot.update(self.inputs, self.robots)
			if self.tilemap.collide_with_danger(robot):
				self.robots.remove(robot)


if __name__ == "__main__":
	import main