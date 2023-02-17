from AppiumFramework.base.BasePage import BasePage


class ActivityPage(BasePage):

    margin = .001
    _homeFragmentLabel = "HomeFragment" # text

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.windowSize = self.driver.get_window_size()
        self.width = self.windowSize['width']
        self.height = self.windowSize['height']

    def swipeRightToLeft(self):
        # From right to left
        try:
            self.TA.long_press(None, self.width - self.margin, self.height / 2).move_to(None, 0, self.height / 2).release().perform()
            self.log("Swipe from right to left successfully", attach=True)
        except:
            self.log("Swipe from right to left FAILED", status="error", attach=True)
            assert False

    def swipeLeftToRight(self):
        try:
            # From left to right
            self.TA.long_press(None, 0, self.height / 2).move_to(None, self.width - self.margin, self.height / 2).release().perform()
            self.log("Swipe from left to right successfully", attach=True)
        except:
            self.log("Swipe from left to right FAILED", status="error", attach=True)
            assert False

    def swipeTopToBottom(self):
        try:
            # From top to bottom
            self.TA.long_press(None, self.width / 2, 0).move_to(None, self.width / 2, self.height - self.margin).release().perform()
            self.log("Swipe from Top to Bottom successfully", attach=True)
        except:
            self.log("Swipe from Top to Bottom FAILED", status="error", attach=True)

    def swipeBottomToTop(self):
        try:
            # From bottom to top
            self.TA.long_press(None, self.width / 2, self.height - self.margin).move_to(None, self.width / 2, 0).release().perform()
            self.log("Swipe from Bottom to Top successfully", attach=True)
        except:
            self.log("Swipe from Bottom to Top FAILED", status="error", attach=True)
            assert False

    def validateActivityLandingPage(self):
        assert True == self.isDisplayed(self._homeFragmentLabel, "text")



