from selenium.webdriver.support.wait import WebDriverWait

from AppiumFramework.base.BasePage import BasePage


class LoginPage(BasePage):

    _enterEmailField = '//android.widget.EditText[@resource-id="com.code2lead.kwad:id/Et4"]'
    _enterPasswordField = '//android.widget.EditText[@resource-id="com.code2lead.kwad:id/Et5"]'
    _loginBtn = '//android.widget.Button[@resource-id="com.code2lead.kwad:id/Btn3"]'
    _wrongCredentialsFlagMsg = 'Wrong Credentials' #text
    _enterAdminField = '//android.widget.EditText[@resource-id="com.code2lead.kwad:id/Edt_admin"]'
    _submitAdminBtn = '//android.widget.Button[@resource-id="com.code2lead.kwad:id/Btn3"]'
    _submittedTextFlag = '//android.widget.TextView[@resource-id="com.code2lead.kwad:id/Tv_admin"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15, poll_frequency=.5)

    def enterEmail(self, email):
        self.sendKeys(email, self._enterEmailField)
        self.log(f"{email} entered correctly on email field")

    def enterPassword(self, password):
        self.sendKeys(password, self._enterPasswordField)
        self.log(f"{password} entered correctly on password field")

    def clickSubmitBtn(self):
        self.clickElement(self._submitAdminBtn)
        self.log("Submit button clicked successfully")

    def enterCredentials(self, email, password, invalidLogin=False):
        self.enterEmail(email)
        self.enterPassword(password)
        self.log(f"{email} - {password} entered correctly on their respective fields", True)
        self.clickSubmitBtn()
        if invalidLogin:
            errorFlagDisplayed = self.isDisplayed(self._wrongCredentialsFlagMsg, 'text')
            self.log(f"errorFlagDisplayed: {errorFlagDisplayed}")
            if errorFlagDisplayed:
                self.log("Invalid credentials entered, negative test passes", True)
                assert True == errorFlagDisplayed
                self.enterKeyCode('4')
            else:
                assert False
        else:
            assert True == self.isDisplayed(self._enterAdminField)
            self.log("Credentials entered correctly", True)

    def enterAdminText(self, textToEnter):
        self.sendKeys(textToEnter, self._enterAdminField)
        assert True == self.isDisplayed(self._submittedTextFlag)




