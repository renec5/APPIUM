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

enterValue = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Btn1"]')))
print("Enter Some Value text on Button: ", enterValue.text)
print("Content Description on Some Value Button: ", enterValue.get_attribute("content-desc"))
enterValue.click()

enterValueKeys = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.EditText[@resource-id="com.code2lead.kwad:id/Et1"]')))

print("Enter Value text: ", enterValueKeys.text)
enterValueKeys.send_keys("Testing")
time.sleep(2)
enterValueKeys.clear()
time.sleep(2)
enterValueKeys.send_keys("Another test")
time.sleep(2)
backButton = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')))
backButton.click()

driver.quit()





