import pygame as pg

class Inputs:
	def __init__(self):
		self.quit = False
		self.keys = {}
		self.keys["left"] = KeyInput(pg.K_LEFT, pg.K_a, pg.K_q)
		self.keys["right"] = KeyInput(pg.K_RIGHT, pg.K_d)
		self.keys["up"] = KeyInput(pg.K_UP, pg.K_z, pg.K_w)
		self.keys["down"] = KeyInput(pg.K_DOWN, pg.K_s)
		self.keys["primary"] = KeyInput(pg.K_SPACE)
		self.keys["secondary"] = KeyInput(pg.K_LCTRL)

	def update(self):
		for key_input in self.keys.values():
			key_input.keydown = False
			key_input.keyup = False
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.quit = True
			if event.type == pg.KEYDOWN:
				for key_input in self.keys.values():
					if event.key in key_input.keys:
						key_input.keydown = True
						key_input.pressed = True
			if event.type == pg.KEYUP:
				for key_input in self.keys.values():
					if event.key in key_input.keys:
						key_input.keyup = True
						key_input.pressed = False


class KeyInput:
	def __init__(self, *keys):
		self.keys = keys
		self.keydown = False
		self.pressed = False
		self.keyup = False


if __name__ == "__main__":
    import main
