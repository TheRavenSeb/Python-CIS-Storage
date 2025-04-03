from modules.Logger import logger

num = 0
logger_instance = logger()
logger_instance.info("Starting the program")
 for i in range(10):
    num += 1
    logger_instance.info(f"Current number: {num}")
    if num == 5:
        logger_instance.warning("Number is 5, taking action")
        # Perform some action here
        break
    
    else:
        pass