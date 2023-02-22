from appium import webdriver


class Driver:

    def __init__(self):
        pass

    # This one has the mobile application settings to make it work and
    # creates and return the driver instance
    def getDriverMethod(self):
        desired_caps = {}

        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'Pixel 3XL'
        desired_caps['app'] = '/Users/rene.cortes/Downloads/Android_Demo_App.apk'
        desired_caps['appPackage'] = 'com.code2lead.kwad'
        desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return driver
