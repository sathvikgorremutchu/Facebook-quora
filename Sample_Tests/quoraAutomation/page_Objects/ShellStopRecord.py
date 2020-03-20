from Sample_Tests.quoraAutomation.Page_Objects.BaseClass import BasePage
import time
import subprocess

class ShellStopRecord(BasePage):
    def stop(self):
        time.sleep(3)
        try:
           self.driver.p1.terminate()
           cmd='adb pull /mnt/sdcard/Download/test.mp4 '+'/Users/lsspldev/IdeaProjects/FacebookAutomation/Sample_Tests/quoraAutomation/Gallery/'
           p2=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
           time.sleep(5)
           p2.terminate()

        except Exception as e :
            print(e)