import os
import time
import allure
from datetime import datetime
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import AppiumFramework.utilities.CustomLogger as cl


class BasePage:

    logger = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15, poll_frequency=.5)

    def getElement(self, locator, locatorType="xpath"):
        locatorType = locatorType.upper()
        if locatorType == "ID":
            element = self.wait.until(EC.presence_of_element_located((AppiumBy.ID, locator)))
        elif locatorType == "CLASS":
            element = self.wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, locator)))
        elif locatorType == "DESC":
            element = self.wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, f'UiSelector().description("{locator}")')))
        elif locatorType == "TEXT":
            element = self.wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{locator}")')))
        elif locatorType == "XPATH":
            element = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, locator)))
        elif locatorType == "INDEX":
            element = self.wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, f'UiSelector().index("{int(locator)}")')))
        else:
            element = None

        if element is not None:
            self.log(f"Element with locatorType: {locatorType} and Locator: {locator} has been found")
        else:
            self.log(f"ERROR Element with locatorType: {locatorType} and Locator: {locator} COULD NOT BE FOUND")
        return element

    def clickElement(self,locator, locatorType="xpath"):
        element = None
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log(f"Element with locatorType: {locatorType} and locator: {locator} has been Clicked Correctly")
        except:
            self.log(f"ERROR Element with locatorType: {locatorType} and locator: {locator} COULD NOT BE CLICKED")

    def sendKeys(self, data, locator, locatorType="xpath"):
        element = None
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log(
                f"Data sent to Element with locatorType: {locatorType} and locator: {locator}")
        except:
            self.log(
                f"ERROR DATA COULD NOT BE SENT TO Element with locatorType: {locatorType} and locator: {locator}")


    def takeScreenshot(self, attach=False, screenshotName="Screenshot", ssSection="ScreenshotSection"):
        fileName = screenshotName + "-" + datetime.now().strftime("%d_%m_%y_%H_%M_%S.%f") + ".png"
        screenshotDirectory =  "/Users/rene.cortes/PycharmProjects/AppiumPython/AppiumFramework/screenshots"
        self.logger.info(f"screenshot directory {screenshotDirectory}")
        screenshotPath = os.path.join(screenshotDirectory, fileName)
        self.logger.info(f"screenshot path {screenshotPath}")
        try:
            self.driver.save_screenshot(screenshotPath)
            # This step can be removed if wanted, this is covered on attachSS method
            self.attachSS(attach, screenshotName, ssSection)
            self.logger.info(f"Screenshot saved to path: {screenshotDirectory}")
        except:
            self.logger.error(f"ERROR - Unable to save Screenshot to path: {screenshotPath}")

    def isDisplayed(self, locator, locatorType="xpath"):
        element = None
        try:
            element = self.getElement(locator, locatorType)
            if element.is_displayed():
                return True
        except:
            return False

    def log(self, text, attach=False, status="info", ScreenshotSection=""):
        status = status.upper()
        if attach:
            with allure.step(text):
                allure.attach(self.driver.get_screenshot_as_png(), name=ScreenshotSection, attachment_type=AttachmentType.PNG)
                if status == "INFO":
                    self.logger.info(text)
                elif status == "ERROR":
                    self.logger.error(text)
        else:
            with allure.step(text):
                pass

    def enterKeyCode(self, keyCodeToEnter):
        self.driver.press_keycode(int(keyCodeToEnter))



