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
    def test_1(self):
        self.CM.printTestname("Test1")
        self.MP.clickEnterSomeValue()
        self.ESVP.validateContactUsFormLandingPage()
        self.ESVP.enterSomeValueText("This is just a test")
        self.ESVP.clickSubmitBtn()



"""
enterValue = BP.getElement('com.code2lead.kwad:id/EnterValue', 'id')
enterValue.click()

inputField = BP.getElement("android.widget.EditText", 'class')
inputField.send_keys("Just a test")
"""





