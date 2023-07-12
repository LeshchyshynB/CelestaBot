from .settings import *
from . import settings
from .log_writer import ConsoleLogWriter, FileLogWriter

#My loger --> 
class Logging:
	writers = [
		ConsoleLogWriter(min_log=settings.MIN_TO_CONSOLE)
		# FileLogWriter(min_log=settings.MIN_TO_LOG)
		]

	@classmethod
	def notset(cls, message):
		cls._process_writers(message, Levels.NOTSET)
	
	@classmethod
	def debug(cls, message):
		cls._process_writers(message, Levels.DEBUG)

	@classmethod
	def info(cls, message):
		cls._process_writers(message, Levels.INFO)

	@classmethod
	def warning(cls, message):
		cls._process_writers(message, Levels.WARNING)

	@classmethod
	def error(cls, message):
		cls._process_writers(message, Levels.ERROR)

	@classmethod
	def critical(cls, message):
		cls._process_writers(message, Levels.CRITICAL)

	@classmethod
	def setting(cls, min_console=30, min_log=10, writer=None):
		settings.MIN_TO_LOG = min_log
		settings.MIN_TO_CONSOLE = min_console
		

		if writer:
			cls.writers = writer

	@classmethod
	def _process_writers(cls, message, level):
		for writer in cls.writers:
			writer.handle(message, level)