import pygame as pg
from settings import *

class TileMap:
	def __init__(self, width, height, data):
		self.width = width
		self.height = height
		self.tiles = [[Tile(i, j, data) for i in range(self.width)] for j in range(self.height)]

	def get_image(self, x, y):
		return self.tiles[y][x].get_image()

	def set_dangerous(self, x, y):
		self.tiles[y][x].dangerous = True

	def set_safe(self, x, y):
		self.tiles[y][x].dangerous = False

	def set_all_safe(self):
		for y in range(self.height):
			for x in range(self.width):
				self.tiles[y][x].dangerous = False

	def collide_with_danger(self, robot):
		for y in range(self.height):
			for x in range(self.width):
				if self.tiles[y][x].dangerous and self.tiles[y][x].collide(robot):
					return True
		return False


class Tile:
	def __init__(self, x, y, data):
		self.data = data
		self.pos = (x, y)
		self.dangerous = False

		self.rect = pg.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)

	def get_image(self):
		if self.dangerous:
			return self.data.texture_tile_danger
		else:
			return self.data.texture_tile


	def collide(self, robot):
		return self.rect.collidepoint(robot.position)

if __name__ == "__main__":
    import main