from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

enterValue = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]')))
print("Is Displayed: {0}".format(enterValue.is_displayed()))
print("Is enabled: {0}".format(enterValue.is_enabled()))
print("Is Selected: {0}".format(enterValue.is_selected()))
print("Size: {0}".format(enterValue.size))
print("Location: {0}".format(enterValue.location))