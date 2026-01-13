import pygame as pg
from settings import *


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
		self.texture_robot_screen_next = pg.image.load("./data/textures/robot_screen_next.png").convert()
		self.texture_screen_neige = [pg.image.load(f"./data/textures/screen_neige_{i+1}.png").convert_alpha() for i in range(3)]

		self.easy_levels = []
		self.normal_levels = []
		self.hard_levels = []
		self.generate_levels()

	def generate_levels(self):
	# HARD
		# left block
		level = []
		for y in range(TILEMAP_HEIGHT):
			for x in range(int(TILEMAP_WIDTH/2)):
				level.append((x,y))
		self.hard_levels.append(level)

		# right block
		level = []
		for y in range(TILEMAP_HEIGHT):
			for x in range(int(TILEMAP_WIDTH/2), TILEMAP_WIDTH):
				level.append((x,y))
		self.hard_levels.append(level)
		
		# top block
		level = []
		for y in range(int(TILEMAP_HEIGHT/2)):
			for x in range(TILEMAP_WIDTH):
				level.append((x,y))
		self.hard_levels.append(level)
		
		# top block
		level = []
		for y in range(int(TILEMAP_HEIGHT/2), TILEMAP_HEIGHT):
			for x in range(TILEMAP_WIDTH):
				level.append((x,y))
		self.hard_levels.append(level)
		
	# NORMAL
		# diagonal
		level = []
		for i in range(TILEMAP_HEIGHT):
			level.append((i,i))
		self.hard_levels.append(level)
		
		# diagonal trans
		level = []
		for i in range(TILEMAP_HEIGHT):
			level.append((i,TILEMAP_HEIGHT-i-1))
		self.hard_levels.append(level)

		# left block
		level = []
		for y in range(TILEMAP_HEIGHT):
			for x in range((int(TILEMAP_WIDTH/2))-1):
				level.append((x,y))
		self.normal_levels.append(level)

		# right block
		level = []
		for y in range(TILEMAP_HEIGHT):
			for x in range(1+(int(TILEMAP_WIDTH/2)), TILEMAP_WIDTH):
				level.append((x,y))
		self.normal_levels.append(level)
		
		# top block
		level = []
		for y in range((int(TILEMAP_HEIGHT/2))-1):
			for x in range(TILEMAP_WIDTH):
				level.append((x,y))
		self.normal_levels.append(level)
		
		# top block
		level = []
		for y in range(1+(int(TILEMAP_HEIGHT/2)), TILEMAP_HEIGHT):
			for x in range(TILEMAP_WIDTH):
				level.append((x,y))
		self.normal_levels.append(level)

		# center block
		self.normal_levels.append([(2,2), (2,3), (3,2), (3,3)])

	# EASY
		#corners
		self.easy_levels.append([(0,0), (5,5), (0,5), (5,0)])

if __name__ == "__main__":
    import main 
