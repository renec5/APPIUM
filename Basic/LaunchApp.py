from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel 3XL'
desired_caps['app'] = '/Users/rene.cortes/Downloads/Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

enterValue = driver.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/EnterValue')
enterValue.click()

input = driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.EditText")
input.send_keys("Testing")

submitBtn = driver.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Btn1')
submitBtn.click()

preview = driver.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Tv1')
print(preview.text)

