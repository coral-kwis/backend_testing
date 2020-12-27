import inspect
import logging
import os
from datetime import datetime

from src.commons import constants


def logger():
    LOGFILE_PATH = os.path.join(constants.ROOT_DIR, '..', 'logs',
                                f'{datetime.now().strftime("%Y-%m-%d")}.log')
    loggerName = inspect.stack()[1][3]
    myLogger = logging.getLogger(loggerName)
    fileHandler = logging.FileHandler(LOGFILE_PATH)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(filename)s : %(name)s : %(message)s')
    fileHandler.setFormatter(formatter)
    myLogger.handlers.clear()
    myLogger.addHandler(fileHandler)
    myLogger.setLevel(logging.DEBUG)
    return myLogger

# myLogger.handlers.clear() : Since Python 3.2 you can just check if handlers are already present and if so, clear them before adding new handlers.
# It can help you develop a better understanding of the flow of a program
# and discover scenarios that you might not even have thought of while developing.
