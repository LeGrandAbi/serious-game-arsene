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

		self.robots = [Robot(self.data) for _ in range(NB_ROBOTS)]
		self.controlled_robot = self.robots[0]
		self.next_robot = self.robots[1]
		self.switch_robot_control()

		self.current_level = self.data.easy_levels[randint(0, len(self.data.easy_levels)-1)]
		self.level_timer = 0
		self.level_period = LEVEL_PERIOD_MAX * 60

	def update(self):
		self.update_robots()
		self.update_level()

	def update_robots(self):
		if self.inputs.keys["primary"].keydown:
			self.switch_robot_control()
		for robot in self.robots:
			robot.update(self.inputs, self.robots, self.controlled_robot)
			if self.tilemap.collide_with_danger(robot) or robot.life < 1:
				if robot.controlled:
					self.switch_robot_control()
				elif robot.is_next: 
					self.next_robot.is_next = False
					self.next_robot = self.robots[randint(0, len(self.robots)-1)]
					while (self.next_robot == self.controlled_robot) and (len(self.robots) > 1):
						self.next_robot = self.robots[randint(0, len(self.robots)-1)]
					self.next_robot.is_next = True
				self.robots.remove(robot)

	def update_level(self):
		if self.level_timer == self.level_period/4:
			self.tilemap.set_warnings(self.current_level)
		elif self.level_timer == self.level_period*3/4:
			self.tilemap.set_dangers(self.current_level)
		elif self.level_timer == self.level_period:
			self.tilemap.clear_level()
		elif self.level_timer > self.level_period:
			self.level_timer = 0
			self.level_period = max(LEVEL_PERIOD_MIN*60, self.level_period - (LEVEL_PERIOD_MALUS*60))
			self.change_level()
		self.level_timer += 1

	def change_level(self):
		r = randint(1,LEVEL_WEIGHT_EASY + LEVEL_WEIGHT_NORMAL + LEVEL_WEIGHT_HARD)
		if r <= LEVEL_WEIGHT_EASY :
			new_lvl = self.data.easy_levels[randint(0, len(self.data.easy_levels)-1)]
		elif r <= LEVEL_WEIGHT_EASY + LEVEL_WEIGHT_NORMAL :
			new_lvl = self.data.normal_levels[randint(0, len(self.data.normal_levels)-1)]
		else:
			new_lvl = self.data.hard_levels[randint(0, len(self.data.hard_levels)-1)]
		self.current_level = new_lvl

	def switch_robot_control(self):
		if len(self.robots) > 1:
			self.controlled_robot.controlled = False
			self.controlled_robot = self.next_robot
			self.controlled_robot.controlled = True
			self.controlled_robot.is_next = False
			self.next_robot = self.robots[randint(0, len(self.robots)-1)]
			while (self.next_robot == self.controlled_robot):
				self.next_robot = self.robots[randint(0, len(self.robots)-1)]
			self.next_robot.is_next = True

	def draw_display(self):
		for x in range(self.tilemap.width):
			for y in range(self.tilemap.height):
				texture = self.tilemap.get_image(x, y)
				self.display.blit(texture, (x*TILE_SIZE, y*TILE_SIZE))

		for robot in sorted(self.robots, key = lambda robot: robot.position.y):
			texture = robot.get_image()
			self.display.blit(texture, texture.get_rect(center=robot.position))

	def exit_condition(self):
		return len(self.robots) < 3


if __name__ == "__main__":
	import main