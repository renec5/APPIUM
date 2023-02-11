import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel3XL'
desired_caps['app'] = '/Users/rene.cortes/Downloads/Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps);
wait = WebDriverWait(driver, 15, poll_frequency=.5)

acceptContinueBtn = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.android.chrome:id/terms_accept")))
acceptContinueBtn.click()

noThanksBtn1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@resource-id='com.android.chrome:id/negative_button']")))
noThanksBtn1.click()

noThanksBtn2 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.android.chrome:id/feed_stream_recycler_view')))
noThanksBtn2.click()

searchBar = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='com.android.chrome:id/search_box_text']")))
searchBar.send_keys("www.google.com/")
driver.press_keycode(66)
time.sleep(5)

appContexts = driver.contexts
print("AppContexts: {0}".format(appContexts))

for app in appContexts:
    if app == "WEBVIEW_chrome":
        driver.switch_to.context(app)
        break

# print(driver.context)

searchBarWebView = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='q']")))
searchBarWebView.send_keys("Skill2Lead")
driver.press_keycode(66)

time.sleep(5)

for app in appContexts:
    if app == "NATIVE_APP":
        driver.switch_to.context(app)
        break

# print(driver.context)
time.sleep(3)
driver.quit()



