from time import sleep
from keys import KEY_MAPPING
import ctypes

class Moves(KEY_MAPPING):
	def __init__(self):
		super(Moves, self).__init__()		
		#init buttons
		self.jump = self.get_key("c")
		self.right = self.get_key("right")
		self.left = self.get_key("left")
		self.dash = self.get_key("x")
		self.up = self.get_key("up")
		self.down = self.get_key("down")
		self.catch = self.get_key("z")

	#catch wall
	def climb_up(self, time):
		self.hold_press([self.catch], self.up, time)

	def climb_down(self, time):
		self.hold_press([self.catch], self.down, time)

	def climb_jump(self, time):
		self.hold_press([self.catch, self.up], self.jump, time)


	#standart move
	def move_jump(self, time):
		self.press_button(self.jump, time)

	def move_right(self, time):
		self.press_button(self.right, time)

	def move_left(self, time):
		self.press_button(self.left, time)

	def move_dash(self, time):
		self.press_button(self.dash, time)


	#diagonal jumps
	def jump_right(self, time):
		self.hold_press([self.right], self.jump, time)

	def jump_left(self, time):
		self.hold_press([self.left], self.jump, time)


	#standart dashes
	def dash_right(self, time):
		self.hold_press([self.right], self.dash, time)

	def dash_left(self, time):
		self.hold_press([self.left], self.dash, time)

	def dash_up(self, time):
		self.hold_press([self.up], self.dash, time)

	def dash_down(self, time):
		self.hold_press([self.down], self.dash, time)
	

	#diafonal dashes
	def dash_up_right(self, time):
		self.hold_press([self.up, self.right], self.dash, time)

	def dash_up_left(self, time):
		self.hold_press([self.up, self.left], self.dash, time)

	def dash_down_right(self, time):
		self.hold_press([self.down, self.right], self.dash, time)

	def dash_down_left(self, time):
		self.hold_press([self.down, self.left], self.dash, time)

	#longjumps
	def long_jump_right(self, time):
		self.hold_press([self.right, self.jump], self.dash, time)

	def long_jump_left(self, time):
		self.hold_press([self.left, self.jump], self.dash, time)