import os
import time
from base64 import b64decode
from Sample_Tests.quoraAutomation.Page_Objects.BaseClass import BasePage


class screenRecord(BasePage):

    def record(self):

        raw_Video=self.driver.stop_recording_screen()
        vid_Name=self.driver.current_activity+time.strftime("%Y_%m_%d_%H%M%S")

        filepath=os.path.join("/Sample_Tests/quoraAutomation/Gallery/", vid_Name + ".mp4")
        with open(filepath,"wb") as vd:
            vd.write(b64decode(raw_Video))



