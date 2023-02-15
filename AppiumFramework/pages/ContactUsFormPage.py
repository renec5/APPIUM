from selenium.webdriver.support.wait import WebDriverWait
from AppiumFramework.base.BasePage import BasePage
import AppiumFramework.utilities.CustomLogger as CL


class EnterSomeValuePage(BasePage):

    _enterSomeValueField = '//android.widget.EditText[@resource-id="com.code2lead.kwad:id/Et1"]'
    _submitBtn = '//android.widget.Button[@resource-id="com.code2lead.kwad:id/Btn1"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15, poll_frequency=.5)

    def validateContactUsFormLandingPage(self):
        assert True == self.isDisplayed(self._enterSomeValueField)
        CL.allureLogs("Contact Us Form Page Reached Successfully")
        self.takeScreenshot(ssSection="EnterSomeValueLandingPage")

    def enterSomeValueText(self, textToEnter):
        self.sendKeys(textToEnter, self._enterSomeValueField)
        self.log(f"{textToEnter}, entered correclty on field", True)
        # CL.allureLogs(f"{textToEnter} entered Successfully on enter some value field")
        self.takeScreenshot(ssSection="EnterSomeValueData")

    def clickSubmitBtn(self):
        self.clickElement(self._submitBtn)
        CL.allureLogs("Submit button clicked successfully on entersome value section")



