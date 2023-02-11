import unittest
import pytest
from AppiumFramework.base.BasePage import BasePage
from AppiumFramework.pages.EnterSomeValuePage import EnterSomeValuePage
from AppiumFramework.pages.MainPage import MainPage


@pytest.mark.usefixtures("oneTimeSetUp")
class testContactUsForm(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.MP = MainPage(self.driver)
        self.ESVP = EnterSomeValuePage(self.driver)
        self.BP = BasePage(self.driver)

    def test1(self):
        self.MP.clickEnterSomeValue()
        self.ESVP.validateContactUsFormLandingPage()
        self.ESVP.enterSomeValueText("This is just a test")
        self.BP.log("All Data entered correctly", attach=True)
        self.ESVP.clickSubmitBtn()



"""
enterValue = BP.getElement('com.code2lead.kwad:id/EnterValue', 'id')
enterValue.click()

inputField = BP.getElement("android.widget.EditText", 'class')
inputField.send_keys("Just a test")
"""





