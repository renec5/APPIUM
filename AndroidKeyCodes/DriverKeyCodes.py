"""
We can search appium keycodes in google, this keycodes simulate keys
from our keyboard, if we need to use same key multiple times we can do it
either by using the same command many times or with a for loop but for loop
performs very slow, it is better to use selenium methods like element.clear()
this works faster
"""

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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
enterValue.click()

enterText = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.EditText[@resource-id="com.code2lead.kwad:id/Et1"]')))
enterText.send_keys("Testing keycodes")
"""
for i in range(15):
    enterText.click()
    driver.press_keycode(67)
"""
enterText.clear()
driver.press_keycode(4)

driver.quit()

