# -*- encoding=utf8 -*-
_author_ = "12064"

from airtest.core.api import *
import time
from poco.exceptions import PocoNoSuchNodeException
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# Open file connection
# ft = open(r"C:\\Users\\12064\\Desktop\\table.csv", "w+")

# Search elderly
poco("com.ss.android.ugc.aweme:id/b9_").click()
poco("com.ss.android.ugc.aweme:id/ah7").set_text("姥爷")
sleep(2)
poco("android:id/content").offspring("com.ss.android.ugc.aweme:id/cu2").child("android.widget.LinearLayout")[0].child("com.ss.android.ugc.aweme:id/ebd").click() 
#poco(text="爷爷").click()
poco(text="视频").click()

# Start of iteration, writes collected titles onto the file
for n in range(100):
    clips = poco("android:id/content").child("android.widget.FrameLayout").offspring("com.ss.android.ugc.aweme:id/eo7").offspring("com.ss.android.ugc.aweme:id/bow").child("android.widget.LinearLayout")
    prevTitle = []
    for clip in clips:
        try:
            title = clip.child("com.ss.android.ugc.aweme:id/brg").offspring("com.ss.android.ugc.aweme:id/a87").get_text()
            if title != prevTitle:
                prevTitle = clip.child("com.ss.android.ugc.aweme:id/brg").offspring("com.ss.android.ugc.aweme:id/a87").get_text()
                with open(r"C:\\Users\\12064\\Desktop\\姥爷.csv", "a+", encoding="utf8", errors="ignore") as f:
                    f.write(title + '\n')
                    f.close()
        except PocoNoSuchNodeException:
            pass
    poco("com.ss.android.ugc.aweme:id/cul").swipe([0.0355, -0.9446])
    sleep(3)