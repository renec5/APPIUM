import pytest
import shutil
import os
from AppiumFramework.base.DriverClass import Driver

@pytest.fixture(scope="class")
def oneTimeSetUp(request):
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    reportsFilesPath = "/Users/rene.cortes/PycharmProjects/AppiumPython/AppiumFramework/reports/allureReports"
    shutil.rmtree(reportsFilesPath)
    os.mkdir(reportsFilesPath)



    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def cleanReportFolder():
    shutil.rmtree("../reports/allureReports")
