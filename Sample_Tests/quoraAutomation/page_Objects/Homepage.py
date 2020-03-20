from Sample_Tests.quoraAutomation.Page_Objects.BaseClass import BasePage
from appium.webdriver.common.mobileby import By
import time
class Homepage(BasePage):

    homeButton=(By.XPATH,'//android.widget.RelativeLayout//android.widget.ImageView[@content-desc="Me"]')
    moreOptions=(By.XPATH,"//android.widget.Button[@text='More options']")
    logout_Option=(By.XPATH,"//android.widget.TextView[@text='Logout']")
    confirm_Logout=(By.XPATH,"//android.widget.Button[@text='Logout']")

    def navigate_To_Logout(self, ):
        time.sleep(10)
        self.driver.find_element(*Homepage.homeButton).click()
        self.driver.find_element(*Homepage.moreOptions).click()
        self.driver.find_element(*Homepage.logout_Option).click()

        return self.driver.find_element(*Homepage.confirm_Logout)



