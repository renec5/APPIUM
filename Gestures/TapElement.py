import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from appium.webdriver.common.touch_action import TouchAction


desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel 3XL'
desired_caps['app'] = '/Users/rene.cortes/Downloads/Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
wait = WebDriverWait(driver, 15, poll_frequency=.5)

touchActions = TouchAction(driver)
"""
to get the coordinates, on the phone virtual device we have to go 
to settings > system > Advanced > Developer options > Input > Enable Pointer location.
When this is done, if we click and hold on any part of the screen, it will give us the
coordinates.
"""
touchActions.tap(None, 550, 1360, 1).perform()

time.sleep(2)

driver.quit()