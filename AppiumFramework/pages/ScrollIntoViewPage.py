from selenium.webdriver.support.wait import WebDriverWait
from AppiumFramework.base.BasePage import BasePage


"""
This page contains locators and methods related to SrollIntoView section
"""

class ScrollIntoViewPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15, poll_frequency=.5)

    def scrollIntoView(self, textOnElementToScroll, click=False):
        element = self.scrollElementIntoView(textOnElementToScroll)
        if click:
            element.click()
            self.log(f"{textOnElementToScroll} has been clicked after Scroll Into View")

    def acceptCancelAlertPopUp(self, yesNoOption="NO"):
        yesNoOption = yesNoOption.upper()
        self.clickElement(yesNoOption, "text")

    def validateCancellingPopUpAlert(self, textOnElementToScroll):
        assert True == self.isDisplayed("BUTTON13", "text")
        self.log(f"PopUp alert has been cancelled successfully and {textOnElementToScroll} is displayed again", True)





