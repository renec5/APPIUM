from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


# @pytest.mark.flaky(reruns=2)
def test_rerunFailedTests():

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
    # this is the correct xpath '//android.widget.Button[@content-desc="Btn1"]' on the element it has been modified
    # to make it fail intentionally and test rerun functionality
    enterValue = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="Btn1"]')))

"""
if we use this fixture we execute the command on terminal normally andfailed tests will be executed the number 
of times we specified on the fixture, but using this notation we need to pass the fixture to every test

or we pass the reruns argument through command line and it will be consider to all test cases at once
py.test -s -v --reruns 1 --reruns-delay 2 RerunTestsPytest/ReRunningFailedTests.py
"""
# py.test -s -v --reruns 1 --reruns-delay 2 RerunTestsPytest/ReRunningFailedTests.py