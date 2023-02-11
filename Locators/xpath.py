from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

zzz = 1
desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel 3XL'
desired_caps['app'] = '/Users/rene.cortes/Downloads/Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# if I change @resource-id for @id it does not find the element
enter_value = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]')
enter_value.click()

time.sleep(zzz)

enterText = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.code2lead.kwad:id/Et1"]')
enterText.send_keys("Testing Xpaths")
time.sleep(zzz)

submitBtn = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.code2lead.kwad:id/Btn1"]')
submitBtn.click()
time.sleep(zzz)

returnBtn = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
returnBtn.click()

time.sleep(zzz)

conactUsBtn = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Btn2"]')
conactUsBtn.click()

time.sleep(zzz)

enterName = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Enter Name"]')
enterName.send_keys("Rene")

enterEmail = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Enter Email"]')
enterEmail.send_keys("test@gmail.com")

enterAddress = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Enter Address"]')
enterAddress.send_keys("Mexico")

enterMobileNo = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Enter Mobile No"]')
enterMobileNo.send_keys("1234567890")

submitContactUsBtn = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="SUBMIT"]')
submitContactUsBtn.click()

time.sleep(zzz)

returnBtn = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
returnBtn.click()
time.sleep(zzz)

driver.quit()



