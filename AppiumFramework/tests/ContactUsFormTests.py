import unittest
import pytest
from AppiumFramework.base.BasePage import BasePage
from AppiumFramework.base.CommonMethods import CommonMethods
from AppiumFramework.pages.ContactUsFormPage import EnterSomeValuePage
from AppiumFramework.pages.MainPage import MainPage


@pytest.mark.usefixtures("oneTimeSetUp", "cleanLogs")
class TestContactUsForm(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp, cleanLogs):
        self.MP = MainPage(self.driver)
        self.ESVP = EnterSomeValuePage(self.driver)
        self.CM = CommonMethods()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_enter_some_value(self):
        self.CM.printTestname("Test1")
        textToEnter = "test"
        self.MP.clickEnterSomeValue()
        self.ESVP.validateContactUsFormLandingPage()
        self.ESVP.enterSomeValueText(textToEnter)
        self.ESVP.clickSubmitBtn()



"""
enterValue = BP.getElement('com.code2lead.kwad:id/EnterValue', 'id')
enterValue.click()

inputField = BP.getElement("android.widget.EditText", 'class')
inputField.send_keys("Just a test")
"""





