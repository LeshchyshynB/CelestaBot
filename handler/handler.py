import os
from moves import Moves
from datetime import datetime
from celesta_logging.logging import Logging

class Handler(Moves):
	def __init__(self, path):
		super(Handler, self).__init__()
		Logging.info("Create variables...")
		self.command_shortcuts = {
			"cd": self.climb_down, 
			"cu": self.climb_up, 
			"dd": self.dash_down, 
			"ddl": self.dash_down_left, 
			"ddr": self.dash_down_right, 
			"dl": self.dash_left, 
			"dr": self.dash_right, 
			"du": self.dash_up, 
			"dul": self.dash_up_left, 
			"dur": self.dash_up_right, 
			"jl": self.jump_left, 
			"jr": self.jump_right, 
			"d": self.move_dash, 
			"j": self.move_jump, 
			"l": self.move_left, 
			"r": self.move_right,
			"ljr": self.long_jump_right,
			"ljl": self.long_jump_left,
			"cj": self.climb_jump
			}

		self.command_list = []
		self.timing_list = []

		Logging.info("Listening files...")
		self.get_moves_from_file(path)
		Logging.info("Let`s go!")
		self.executor()

	def get_moves_from_file(self, path):
		with open(path, 'r') as file:
			for i in file:
				l=i.split(" ")
				self.command_list.append(self.command_translator(l[0]))
				self.timing_list.append(l[1][:-1])

	def command_translator(self, command):
		return self.command_shortcuts[command]
		
	def executor(self):
		for i in range(len(self.command_list)):
			self.command_list[i](float(self.timing_list[i]))