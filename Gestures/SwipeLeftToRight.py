from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
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

TA = TouchAction(driver)

tabActivity = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@resource-id="com.code2lead.kwad:id/TabView"]')))
tabActivity.click()

windowSize = driver.get_window_size()
print("Window Size: {0}".format(windowSize))
width = windowSize['width']
height = windowSize['height']
margin = .001
print(width*8/9)

# From right to left
TA.long_press(None, width-margin, height/2).move_to(None, 0, height/2).release().perform()
# From left to right
TA.long_press(None, 0, height/2).move_to(None, width-margin, height/2).release().perform()

# From top to bottom
TA.long_press(None, width/2, 0).move_to(None, width/2, height-margin).release().perform()
# From bottom to top
TA.long_press(None, width/2, height-margin).move_to(None, width/2, 0).release().perform()

driver.quit()
