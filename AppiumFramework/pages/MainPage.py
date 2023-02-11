from selenium.webdriver.support.wait import WebDriverWait
from AppiumFramework.base.BasePage import BasePage
import AppiumFramework.utilities.CustomLogger as CL

class MainPage(BasePage):

    _enterSomeValueBtn = '//android.widget.Button[@content-desc="Btn1"]'
    _contactyUsFormBtn = '//android.widget.Button[@content-desc="Btn2"]'
    _scrollViewBtn = '//android.widget.Button[@content-desc="Btn3"]'
    _tabActivityBtn = '//android.widget.Button[@content-desc="Btn4"]'
    _zoomBtn = '//android.widget.Button[@content-desc="Btn5"]'
    _loginBtn = '//android.widget.Button[@content-desc="Btn6"]'
    _longClickBtn = '//android.widget.Button[@content-desc="Btn7"]'
    _timeBtn = '//android.widget.Button[@content-desc="Btn8"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15, poll_frequency=.5)

    def clickEnterSomeValue(self):
        self.clickElement(self._enterSomeValueBtn)
        CL.allureLogs("Enter Some Value Button clicked successfully")

    def clickLoginButton(self):
        self.clickElement(self._loginBtn)
        self.log("Login Button clicked correctly")



