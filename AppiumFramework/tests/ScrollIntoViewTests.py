import unittest
import pytest

from AppiumFramework.base.CommonMethods import CommonMethods
from AppiumFramework.pages.MainPage import MainPage
from AppiumFramework.pages.ScrollIntoViewPage import ScrollIntoViewPage


@pytest.mark.usefixtures("oneTimeSetUp", "cleanLogs")
class TestScrollIntoView(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp, cleanLogs):
        self.MP = MainPage(self.driver)
        self.SIVP = ScrollIntoViewPage(self.driver)

    @pytest.mark.regression
    def test_scroll_element_into_view(self):
        textOnElementToScroll = "BUTTON13"
        popUpAlertOption = "no"
        self.MP.clickScrollViewButton()
        self.SIVP.scrollIntoView(textOnElementToScroll, True)
        self.SIVP.acceptCancelAlertPopUp(popUpAlertOption)
        self.SIVP.validateCancellingPopUpAlert(textOnElementToScroll)


