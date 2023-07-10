from .levels.c1_0 import C1_0


class Handler():
	def __init__(self, command):
		self.commands = {
		"C1_0": C1_0
		}
		self.run_command(command)

	def run_command(self, command):
		return self.commands[command]()