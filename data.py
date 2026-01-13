import pygame as pg 


class Data:
	def __init__(self):
		self.texture_tile = pg.image.load("./data/textures/tile.png").convert()
		self.texture_tile_danger = pg.image.load("./data/textures/tile_danger.png").convert()
		self.texture_robot = pg.image.load("./data/textures/robot.png").convert_alpha()

		self.levels = {
			"easy" : [
				[(0,0), (5,5), (0,5), (5,0)],
				[(2,2), (2,3), (3,2), (3,3)],
			],
			"normal" : [
			],
			"hard" : [
			],
		}


if __name__ == "__main__":
    import main