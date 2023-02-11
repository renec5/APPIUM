from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction

"""
{
  "platformName": "Android",
  "appium:automationName": "UiAutomator2",
  "appium:PlatformVersion": "12",
  "appium:deviceName": "Pixel XL Harley",
  "appium:app": "/Users/rene.cortes/Downloads/Harley-Davidson_2.0.20230116_Apkpure.apk",
  "appium:appPackage": "com.harley_davidson.ride_planner",
  "appium:appActivity": "com.harleydavidson.rideplanner.onboarding.WelcomeActivity"
}
"""
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = 'Pixel XL Harley'
desired_caps['app'] = '/Users/rene.cortes/Downloads/Harley-Davidson_2.0.20230116_Apkpure.apk'
desired_caps['appPackage'] = 'com.harley_davidson.ride_planner'
desired_caps['appActivity'] = 'com.harleydavidson.rideplanner.onboarding.WelcomeActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
wait = WebDriverWait(driver, 15, poll_frequency=.5)

