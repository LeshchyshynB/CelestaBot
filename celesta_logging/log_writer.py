from abc import ABC, abstractmethod
from . import settings

class LogWriterBase(ABC):
	def __init__(self, min_log=10):
		self.min_log = min_log
		self.log_template = "{0} | [{1}] |: {2}"

	def handle(self, message, level):
		if self.min_log >= int(level):
			self.write(message, level)

	@abstractmethod
	def write(self, message, level):
		...


class FileLogWriter(LogWriterBase):
	def write(self, message, level):
		with open(settings.DIRECTORY_PATH(), 'a') as file:
			file.write(self.log_template.format(level.name, settings.CURRENT_TIME(), message)+"\n")


class ConsoleLogWriter(LogWriterBase):
	def write(self, message, level):
		print(level.get_color() + self.log_template.format(level.name, settings.CURRENT_TIME(), message))