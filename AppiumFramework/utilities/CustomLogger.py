import logging
import inspect
import allure


def customLogger(loggingLevel=logging.DEBUG):

    logName = inspect.stack()[1][3]

    logger = logging.getLogger(logName)
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("../AppiumPython/AppiumFramework/reports/Code2LEad.log", 'w')
    fileHandler.setLevel(loggingLevel)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M %p")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    return logger

def allureLogs(text):
    with allure.step(text):
        pass
