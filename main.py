from handler.handler import Handler
from time import sleep

class Main():
	def __init__(self, level):
		self.level = level

		sleep(2)
		Handler(level)	

if __name__ == "__main__":
	Main("C1_0")