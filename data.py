import pygame as pg 


class Data:
	def __init__(self):
		self.font = pg.font.Font()

		self.texture_tile = pg.image.load("./data/textures/tile.png").convert()
		self.texture_tile_danger = pg.image.load("./data/textures/tile_danger.png").convert()
		self.texture_tile_warning = pg.image.load("./data/textures/tile_warning.png").convert_alpha()
		self.texture_robot_head_frame = pg.image.load("./data/textures/robot_head_frame.png").convert_alpha()
		self.texture_robot_body_stand = pg.image.load("./data/textures/robot_body.png").convert_alpha()
		self.texture_robot_body_walk_cycle = [pg.image.load(f"./data/textures/robot_body_walk_{i+1}.png").convert_alpha() for i in range(4)]
		self.texture_robot_screen_nosignal = pg.image.load("./data/textures/robot_screen_nosignal.png").convert()
		self.texture_robot_screen_signal = pg.image.load("./data/textures/robot_screen_signal.png").convert()

		self.easy_levels = [
				[(0,0), (5,5), (0,5), (5,0)],
				[(2,2), (2,3), (3,2), (3,3)],
			]
		self.normal_levels = []
		self.hard_levels = []


if __name__ == "__main__":
    import main 
