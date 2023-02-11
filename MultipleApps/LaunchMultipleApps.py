from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

wait = WebDriverWait(driver, 15, poll_frequency=.5)


time.sleep(5)
"""
To run multiple apps on the same code we need to get the appPackage and appActivity of the apps we want to
run, first app will be launched based on our desired_caps settings, but then we can switch between apps
with the line driver.start_activity(appPackage, appActivity) and perform needed actions on each app. 
"""
driver.start_activity('com.google.android.apps.messaging', 'com.google.android.apps.messaging.ui.ConversationListActivity')

time.sleep(5)
driver.start_activity('com.code2lead.kwad', 'com.code2lead.kwad.MainActivity')
time.sleep(5)

driver.quit()
