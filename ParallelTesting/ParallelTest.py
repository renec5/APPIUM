"""
To run parallel testing we need to follow below instructions
1.- pip install pytest-xdist
2.- Add udid and systemPort in desired capabilities
3.- Run the file using command as: pytest -n <numOfProcesses>
4.- systemPort should be between range 8200 - 8299
5.- Command to launch this exexution: we need to pass the hole path to the test file and then
    pytest -n 2
    in this case 2 is the number of parallel tests we will perform
"""

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def deviceDriver(deviceID, systemPort):
    desired_caps = {}

    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = 'Pixel 3XL'
    desired_caps['app'] = '/Users/rene.cortes/Downloads/Android_Demo_App.apk'
    desired_caps['appPackage'] = 'com.code2lead.kwad'
    desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
    desired_caps['udid'] = deviceID
    desired_caps['systemPort'] = systemPort

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    wait = WebDriverWait(driver, 15, poll_frequency=.5)
    return driver

def enterText(driver):
    enterValue = driver.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/EnterValue')
    enterValue.click()

    time.sleep(2)

    inputField = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
    inputField.send_keys("Testing")

def test_deviceTest():
    d1 = deviceDriver('emulator-5554', '8200')
    d2 = deviceDriver('SecondDeviceUDID', 8201)
    enterText(d1)
    enterText(d2)