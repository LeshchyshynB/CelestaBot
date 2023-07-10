from moves import Moves
from time import sleep
import pyautogui

class C1_0(Moves):
	def __init__(self):
		super(C1_0, self).__init__()
		#floor 1
		self.move_right(0.2)
		self.jump_right(0.5)
		self.move_right(0.1)
		self.jump_right(0.5)
		self.climb_up(0.8)
		self.move_right(0.5)
		self.dash_up_right(0.5)
		self.jump_right(0.5)
		self.dash_up(0.5)
		#floor 2
		self.jump_right(0.9)
		sleep(0.05)
		self.jump_right(1)
		self.dash_right(0.5)
		sleep(0.3)
		self.jump_right(0.5)
		self.dash_up_right(0.2)
		self.climb_up(0.1)
		self.jump_left(0.3)
		self.climb_up(0.1)
		self.jump_right(0.3)
		self.climb_up(0.1)
		self.jump_left(0.3)
		self.climb_up(0.1)
		self.jump_right(0.4)
		#floor 3
		sleep(1)
		#pyautogui.alert('This is an alert box.')
		self.move_right(0.3)
		self.jump_right(0.4)
		self.dash_up_right(0.5)
		self.climb_up(0.4)
