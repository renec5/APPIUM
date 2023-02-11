import unittest
import pytest

from AppiumFramework.base.BasePage import BasePage
from AppiumFramework.pages.LoginPage import LoginPage
from AppiumFramework.pages.MainPage import MainPage

@pytest.mark.usefixtures("oneTimeSetUp")
class TestLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.MP = MainPage(self.driver)
        self.LP = LoginPage(self.driver)
        self.BP = BasePage(self.driver)



    def testInvalidLogin(self):
        self.MP.clickLoginButton()
        self.LP.enterCredentials("admin@gmail.com", "abc", True)


    def testValidLogin(self):
        self.MP.clickLoginButton()
        self.LP.enterCredentials("admin@gmail.com", "admin123")
        self.LP.enterAdminText("code2Lead")




