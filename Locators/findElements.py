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

elements = driver.find_elements(AppiumBy.XPATH, '//android.widget.Button[@class="android.widget.Button"]')

for element in elements:
    print(element.text)
    print(element.get_attribute('resource-id'))

for element in elements:
    if element.text == "ScrollView":
        element.click()
        break

time.sleep(1)
driver.quit()
