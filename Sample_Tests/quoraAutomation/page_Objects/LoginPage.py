from Sample_Tests.quoraAutomation.Page_Objects.BaseClass import BasePage
from Sample_Tests.quoraAutomation.Page_Objects.CredentialsPage import CredentialsPage
from appium.webdriver.common.mobileby import By
import time



class LoginPage(BasePage):

    noneOption=(By.XPATH,'//android.widget.LinearLayout[@content-desc="Choose an Account"]/android.widget.LinearLayout/android.widget.Button')
    loginButton=(By.XPATH,"//android.view.View[@text='Login']")



    def logging(self):
        self.driver.find_element(*LoginPage.noneOption).click()
        time.sleep(7)
        self.driver.find_element(*LoginPage.loginButton).click()
        return CredentialsPage(self.driver)
