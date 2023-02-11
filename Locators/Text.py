from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel 3XL'
desired_caps['app'] = '/Users/rene.cortes/Downloads/Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
"""
Both methods below work, if we use the 'new UiSelector().text(""))' single quotes/quotes
have to be in that order otherwise does not work or we can use the other method 
'new UiSelector().text("ENTER SOME VALUE")') which I think is easier
"""
enter_value = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ENTER SOME VALUE")')
# enter_value = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ENTER SOME VALUE")')
enter_value.click()

