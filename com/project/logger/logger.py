import logging
from logging.handlers import RotatingFileHandler
import os

class Logger:
    _instance = None

    @staticmethod
    def get_instance(log_filename="logfile.log"):
        if not Logger._instance:
            Logger(log_filename)
        return Logger._instance

    def __init__(self, log_filename="logfile.log"):
        if Logger._instance:
            raise Exception("This class is designed as a Singleton; obtain its instance using get_instance().")
        else:
            Logger._instance = self

        self.logger = logging.getLogger("CustomLogger")
        self.logger.setLevel(logging.INFO)

        # Get the current working directory
        current_directory = os.getcwd()

        # Create a file handler in the current directory
        log_file_path = os.path.join(current_directory, log_filename)
        handler = RotatingFileHandler(log_file_path, maxBytes=100000, backupCount=1)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_debug(self, message):
        self.logger.debug(message)

    def log_warning(self, message):
        self.logger.warning(message)

if __name__ == "__main__":

    logger = Logger.get_instance("custom_logfile.log")

    # Log messages with different levels
    logger.log_info("This is an informational message.")
    logger.log_error("This is an error message.")
    logger.log_debug("This is a debug message.")
    logger.log_warning("This is a warning message.")
