from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



desired_caps = {}

desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '16.2'
desired_caps['deviceName'] = 'iPhone 11 Pro'
# desired_caps['udid'] = 'C3B2BB2F-09E9-4361-8804-1194E390FB68'
desired_caps['automationName'] = 'XCUITest'
# desired_caps['xcodeOrgid'] = 'G3'
desired_caps['app'] = ('/Users/rene.cortes/Desktop/AppiumCourse/UIKitCatalog.app')


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
wait = WebDriverWait(driver, 15, poll_frequency=.5)

# datePicker = wait.until(EC.element_to_be_clickable((By.XPATH, '//XCUIElementTypeStaticText[@name="Date Picker"]')))
# datePicker = wait.until(EC.element_to_be_clickable((By.ID, 'Date Picker')))
# datePicker = wait.until(EC.element_to_be_clickable((By.XPATH, '//XCUIElementTypeStaticText[@value="Date Picker"]')))
datePicker = wait.until(EC.element_to_be_clickable((By.XPATH, '//XCUIElementTypeStaticText[@label="Date Picker"]')))


datePicker.click()

time.sleep(3)
driver.quit()


