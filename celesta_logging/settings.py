from .libraries import *
from enum import Enum

FILE_FORMAT = "%Y-%m-%d"

CURRENT_FILE = lambda: datetime.now().strftime(FILE_FORMAT)

DIRECTORY_PATH = lambda: f"celesta_logging/logs/{CURRENT_FILE()}.log"

TIME_FORMAT = "%H:%M:%S"

class Levels(Enum): 
	NOTSET = 0, Fore.WHITE
	DEBUG = 10, Fore.WHITE
	INFO = 20, Fore.GREEN
	WARNING = 30, Fore.YELLOW
	ERROR = 40, Fore.MAGENTA
	CRITICAL = 50, Fore.RED

	def __int__(self):
		return self.value[0]

	def get_color(self):
		return self.value[1]

CURRENT_TIME = lambda: datetime.now().strftime(TIME_FORMAT)

MIN_TO_LOG = 10

MIN_TO_CONSOLE = 30
