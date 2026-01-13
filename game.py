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
		self.controlled_robot = self.robots[0]
		self.switch_robot_control()

	def run(self):
		while not self.inputs.quit:
			self.inputs.update()
			self.update()
			self.draw_display()
			self.clock.tick(MAX_FPS)

	def draw_display(self):
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

	def update(self):
		if self.inputs.keys["primary"].keydown:
			self.switch_robot_control()
		for robot in self.robots:
			robot.update(self.inputs, self.robots)
			if self.tilemap.collide_with_danger(robot):
				if robot.controlled: self.switch_robot_control()
				self.robots.remove(robot)


	def switch_robot_control(self):
		self.controlled_robot.controlled = False
		self.controlled_robot = self.robots[rand.randint(0, len(self.robots)-1)]
		self.controlled_robot.controlled = True


if __name__ == "__main__":
	import main