#logger.py
# This module is responsible for logging messages to a file with a timestamp in the filename.
# It uses the logging module from Python's standard library to handle the logging functionality.
# The log file is named with the current date and time to ensure uniqueness and easy identification.
# The log file is created in the same directory as the script.
# The logging level is set to INFO, meaning that all messages at this level and above will be logged.
# The log format includes the timestamp, log level, and the actual message.
    
import logging
from datetime import datetime
import atexit



class logger:
    
    def __init__(self):
        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        # Set up logging configuration
        self.log_file_path = f'logs/log_{timestamp}.log'  # Path to the log file with timestamp
        
        # Create the logs directory if it doesn't exist
        import os
        
        if not os.path.exists('logs'):
            os.makedirs('logs')
            print("Logs directory created.")
            
            
    
        # Ensure the logs directory exists before configuring logging
        if not os.path.exists('logs'):
            os.makedirs('logs')
            print("Logs directory created.")

        # Configure logging
        logging.basicConfig(
            filename=self.log_file_path,  # Use the timestamped log filename
            level=logging.INFO,     # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            format='%(asctime)s - %(levelname)s - %(message)s',  # Log format including timestamp
        )
    
    def info(self, message):
        """
        Log an info message.
        :param message: The message to log.
        """
        logging.info(message)
        print(f"INFO: {message}")
        
    def warning(self, message):
        """
        Log a warning message.
        :param message: The message to log.
        """
        logging.warning(message)
        print(f"WARNING: {message}")

    def error(self, message):
        """
        Log an error message.
        :param message: The message to log.
        """
        logging.error(message)
        print(f"ERROR: {message}")
        
    def critical(self, message):
        """
        Log a critical message.
        :param message: The message to log.
        """
        logging.critical(message)
        print(f"CRITICAL: {message}")
    
    def debug(self, message):
        """
        Log a debug message.
        :param message: The message to log.
        """
        logging.debug(message)
        print(f"DEBUG: {message}")
    def close():
        """
        Close the logger and release any resources.
        """
        logging.shutdown()
        print("Logger closed.")
          
    
        

def close():
        """
        Close the logger and release any resources.
        """
        logging.shutdown()
        print("Logger closed.")
    
atexit.register(close)