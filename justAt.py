import os
import pytest


# os.system('allure serve /Users/rene.cortes/Desktop/COPPELReports')

@pytest.mark.smoke
def test1():
    print("Test Numero 1")

@pytest.mark.smoke
def test2():
    print("Test Numero 2")