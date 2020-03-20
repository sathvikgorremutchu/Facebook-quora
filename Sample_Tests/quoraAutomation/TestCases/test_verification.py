import unittest
from appium import webdriver
from Sample_Tests.quoraAutomation.Page_Objects.LoginPage import LoginPage
from Sample_Tests.quoraAutomation.Page_Objects.Homepage import Homepage
from Sample_Tests.quoraAutomation.Page_Objects.ShellStartRecord import ShellStartRecord
from Sample_Tests.quoraAutomation.Page_Objects.ShellStopRecord import ShellStopRecord

import time



class LoginLogout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                       desired_capabilities=
                                           {
                                               "platformName": "Android",
                                               "platformVersion": "6.0.1",
                                               "deviceName": "android",
                                               "appPackage": "com.quora.android",
                                               "appActivity": "com.quora.android.components.activities.LauncherActivity",
                                               "udid": "320849220ee571bd",
                                               "newCommandTimeout":"70"
                                           }
                                       )
        self.driver.implicitly_wait(50)
        ShellStartRecord(self.driver).record()

        #self.driver.start_recording_screen()



    def test_main(self):

        credentialsPage= LoginPage(self.driver).logging()

        credentialsPage.enterEmail().send_keys('lodestoneq@gmail.com')
        credentialsPage.enterPassword().send_keys('Asdf#123')
        credentialsPage.clicikngDone().click()

        logout_Btn= Homepage(self.driver).navigate_To_Logout()
        logout_Btn.click()
        time.sleep(3)



    def tearDown(self):
       #screenRecord(self.driver).record()
       ShellStopRecord(self.driver).stop()
       self.driver.quit()



if __name__ == '__main__':
    unittest.main()