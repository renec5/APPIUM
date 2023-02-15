# Import needed files and libraries

import unittest
from AppiumFramework.tests.LoginTests import TestLogin
from AppiumFramework.tests.ContactUsFormTests import TestContactUsForm

# Create the object of the class using unittest
CF = unittest.TestLoader().loadTestsFromTestCase(TestContactUsForm)
LT = unittest.TestLoader().loadTestsFromTestCase(TestLogin)

# Create TestSuite
regressionTests = unittest.TestSuite([CF, LT])

# Call TestRunner method
unittest.TextTestRunner(verbosity=1).run(regressionTests)