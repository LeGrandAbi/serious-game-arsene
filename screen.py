from settings import *

class Screen:
	def __init__(self, display, clock, inputs, data):
		self.display = display
		self.clock = clock
		self.inputs = inputs
		self.data = data

	def run(self):
		while not self.inputs.quit:
			self.inputs.update()
			self.update()
			self.draw_display()
			self.clock.tick(MAX_FPS)

	def draw_display(self):
		pass

	def update(self):
		pass