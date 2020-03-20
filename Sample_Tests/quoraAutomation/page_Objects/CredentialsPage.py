from Sample_Tests.quoraAutomation.Page_Objects.BaseClass import BasePage
from appium.webdriver.common.mobileby import By

class CredentialsPage(BasePage):

    emailBtn=(By.XPATH,"//android.view.View[@text='Email']//parent::android.view.View//android.view.View[2]//android.widget.EditText")
    passwordBtn=(By.XPATH,"//android.view.View[@text='Password']//parent::android.view.View//android.view.View[2]//android.widget.EditText")
    doneBtn=(By.XPATH,"//android.widget.TextView[@resource-id='com.quora.android:id/actionview_right_button_0']")
    statusBtn=(By.XPATH,"//android.widget.TextView[@resource-id='com.quora.android:id/message']")
    backBtn=(By.XPATH,"//android.widget.Button[@text='OK']")


    def enterEmail(self):
        return  self.driver.find_element(*CredentialsPage.emailBtn)

    def enterPassword(self):
        return self.driver.find_element(*CredentialsPage.passwordBtn)

    def clicikngDone(self):
        return self.driver.find_element(*CredentialsPage.doneBtn)


