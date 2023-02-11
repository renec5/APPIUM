from appium import webdriver
import time
import subprocess
import IOSAutomation.IOS_LOCATORS as SC


desired_caps = {}

desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '16.2'
desired_caps['deviceName'] = 'iPhone 11 Pro'
# desired_caps['udid'] = 'C3B2BB2F-09E9-4361-8804-1194E390FB68'
desired_caps['automationName'] = 'XCUITest'
# desired_caps['xcodeOrgid'] = 'G3'
desired_caps['app'] = ('/Users/rene.cortes/Desktop/AppiumCourse/UIKitCatalog.app')

# time.sleep(60)
# subprocess.run("python3 IOSAutomation/IOS_LOCATORS.py")
# subprocess.run('chmod +x /Users/rene.cortes/ios.sh && /Users/rene.cortes/./ios.sh', shell=True)
# print("Starting process")
# subprocess.run('chmod +x /Users/rene.cortes/killStartSimulator.sh && /Users/rene.cortes/./killStartSimulator.sh', shell=True)
# subprocess.run('chmod +x /Users/rene.cortes/ios.sh && /Users/rene.cortes/./ios.sh', shell=True)
# subprocess.run('cd /Users/rene.cortes/Downloads/WebDriverAgent-4.9.0 && xcodebuild build-for-testing test -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "platform=iOS Simulator,name=iPhone 11 Pro,OS=16.2" IPHONEOS_DEPLOYMENT_TARGET=16.2 GCC_TREAT_WARNINGS_AS_ERRORS=0 COMPILER_INDEX_STORE_ENABLE=NO CODE_SIGNING_ALLOWED=NO &', shell=True)

# time.sleep(60)
# print("Time Finished")


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
