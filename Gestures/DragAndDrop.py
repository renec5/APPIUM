import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

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

# dragDropBtn = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("DRAGANDDROP")')))
dragDropBtn = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollIntoView(text("DRAGANDDROP"))'))
dragDropBtn.click()

icon = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.code2lead.kwad:id/ingvw")))
target = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.LinearLayout[@resource-id="com.code2lead.kwad:id/layout2"]')))
touchActions = TouchAction(driver)
Actions = ActionChains(driver)
# Actions.drag_and_drop(icon, target)
touchActions.long_press(icon).move_to(target).release().perform()

time.sleep(3)
driver.quit()
