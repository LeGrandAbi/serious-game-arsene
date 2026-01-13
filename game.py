import pygame as pg
from random import randint

from settings import *
from screen import *
from robot import Robot
from tilemap import TileMap


class Game(Screen):
	def __init__(self, display, clock, inputs, data):
		super().__init__(display, clock, inputs, data)
		self.tilemap = TileMap(TILEMAP_WIDTH, TILEMAP_HEIGHT, self.data)
		self.tilemap.set_dangers(self.data.easy_levels[0])
		self.robots = [Robot(self.data) for _ in range(NB_ROBOTS)]
		self.controlled_robot = self.robots[0]
		self.switch_robot_control()

	def draw_display(self):
		for x in range(self.tilemap.width):
			for y in range(self.tilemap.height):
				texture = self.tilemap.get_image(x, y)
				self.display.blit(texture, (x*TILE_SIZE, y*TILE_SIZE))
		for robot in sorted(self.robots, key = lambda robot: robot.position.y):
			texture = robot.get_image()
			self.display.blit(texture, texture.get_rect(center=robot.position))

	def update(self):
		if self.inputs.keys["primary"].keydown:
			self.switch_robot_control()
		for robot in self.robots:
			robot.update(self.inputs, self.robots)
			if self.tilemap.collide_with_danger(robot):
				if robot.controlled: self.switch_robot_control()
				self.robots.remove(robot)

	def switch_robot_control(self):
		new_controlled_robot = self.robots[randint(0, len(self.robots)-1)]
		while (new_controlled_robot == self.controlled_robot) and (len(self.robots) > 1):
			new_controlled_robot = self.robots[randint(0, len(self.robots)-1)]
		self.controlled_robot.controlled = False
		self.controlled_robot = new_controlled_robot
		self.controlled_robot.controlled = True

	def exit_condition(self):
		return len(self.robots) < 5


if __name__ == "__main__":
	import main