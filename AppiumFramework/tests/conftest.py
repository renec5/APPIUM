import time
import pytest
import shutil
import os
from AppiumFramework.base.DriverClass import Driver


"""
This method will be called each time a testClass is executed
it sets the driver instance and quit it at the end of each
test case
"""
@pytest.fixture(scope="class")
def oneTimeSetUp(request):
    driver1 = Driver()
    driver = driver1.getDriverMethod()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()


"""
This method will clean up our previous logs to have a clean report
and without previous runs information
"""
@pytest.fixture(scope="session")
def cleanLogs():
    logFile = open("Code2LEad.log", 'w')
    logFile.close()
    shutil.rmtree("/Users/rene.cortes/PycharmProjects/AppiumPython/AppiumFramework/reports/allureReports")
    # time.sleep(5)
    os.mkdir("/Users/rene.cortes/PycharmProjects/AppiumPython/AppiumFramework/reports/allureReports")
