from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel 3XL'
desired_caps['app'] = '/Users/rene.cortes/Downloads/Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

print("Is device locked? {0}".format(driver.is_locked()))
print("Current Package: {0}".format(driver.current_package))
print("Current Activity: {0}".format(driver.current_activity))
print("Current Context: {0}".format(driver.current_context))
print("Current Orientation: {0}".format(driver.orientation))

