import pygame as pg

class Inputs:
	def __init__(self):
		self.quit = False
		self.keys = {}

		# self.keys[ACTION] = KeyInput(KeyA, KeyB, keyC, ...)
		self.keys["left"] = KeyInput(pg.K_LEFT)
		self.keys["right"] = KeyInput(pg.K_RIGHT)
		self.keys["up"] = KeyInput(pg.K_UP)
		self.keys["down"] = KeyInput(pg.K_DOWN)
		self.keys["primary"] = KeyInput(pg.K_SPACE)
		self.keys["secondary"] = KeyInput(pg.K_e)

	def update(self):
		# updates the value of each input according to their assignated keys
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
		self.keys = keys		# array of pg.keyCodes, all the keys that perform the same actions (ex: left arrow, a, q, ...)
		self.keydown = False	# status of the action: the button was just pressed at this tick
		self.pressed = False	# status: the button is being pressed
		self.keyup = False		# status of the action: the button was just released at this tick
