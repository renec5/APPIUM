import unittest
import pytest
from AppiumFramework.base.CommonMethods import CommonMethods
from AppiumFramework.pages.LoginPage import LoginPage
from AppiumFramework.pages.MainPage import MainPage
import time

"""
py.test test_module.py                # run tests in module
py.test somepath                      # run all tests below path
py.test test_module.py::testmethod    # only run test_method in the test_module
"""

@pytest.mark.usefixtures("oneTimeSetUp")
class TestLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.MP = MainPage(self.driver)
        self.LP = LoginPage(self.driver)
        self.CM = CommonMethods()

    @pytest.mark.smoke
    @pytest.mark.sanity
    def test_InvalidLogin(self):
        self.CM.printTestname("testInvalidLogin")
        self.MP.clickLoginButton()
        self.LP.enterCredentials("admin@gmail.com", "abc", True)

    @pytest.mark.sanity
    def test_ValidLogin(self):
        self.CM.printTestname("testValidLogin")
        self.MP.clickLoginButton()
        self.LP.enterCredentials("admin@gmail.com", "admin123")
        self.LP.enterAdminText("code2Lead")




