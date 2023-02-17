import unittest
import pytest
from AppiumFramework.pages.ActivityPage import ActivityPage
from AppiumFramework.pages.MainPage import MainPage


@pytest.mark.use_fixtures("oneTimeSetUp", "cleanLogs")
class ActivityTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp, cleanLogs):
        self.MP = MainPage(self.driver)
        self.AP = ActivityPage(self.driver)

    @pytest.mark.regression
    def test_swipe4ScreenSides(self):
        self.MP.clickActivityButton()
        self.AP.validateActivityLandingPage()
        self.AP.swipeRightToLeft()
        self.AP.swipeLeftToRight()
        self.AP.swipeTopToBottom()
        self.AP.swipeBottomToTop()

