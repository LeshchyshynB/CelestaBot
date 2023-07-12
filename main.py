from handler.handler import Handler
from time import sleep
import os
from celesta_logging.logging import Logging

class Main():
	def __init__(self, level, wait):
		self.level = level
		self.commands_entry = {
		"C1_0": 'handler/levels/c1_0.txt'
		}
		Logging.setting(min_console=10)
		Logging.info(f"Wait {wait} seconds (alt+tab to game)...")
		sleep(wait)
		Logging.info("Starting level...")
		Handler(self.commands_entry[level])	

if __name__ == "__main__":
	Logging.info("Start program...")
	Main("C1_0", 3)
	Logging.info("Level complete!")