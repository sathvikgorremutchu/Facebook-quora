from Sample_Tests.quoraAutomation.Page_Objects.BaseClass import BasePage
import subprocess




class ShellStartRecord(BasePage):

   def record(self):
      cmd='adb shell screenrecord --verbose /mnt/sdcard/Download/test.mp4'
      self.driver.p1= subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
