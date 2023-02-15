import logging
import AppiumFramework.utilities.CustomLogger as cl

class CommonMethods:

    logger = cl.customLogger(logging.DEBUG)

    def printTestname(self, testName):
        msg = "\n\n\n" + "*" * 80 + "\n" + testName.center(80, "*") + "\n" + "*" * 80 + "\n\n\n"
        self.logger.info(msg)