# -*- encoding=utf8 -*-
__author__ = "12064"

from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

poco("com.ss.android.ugc.aweme:id/b9_").click()
poco("com.ss.android.ugc.aweme:id/ah7").set_text("蔡昀恩")
sleep(2)
poco("android:id/content").offspring("com.ss.android.ugc.aweme:id/cu2").child("android.widget.LinearLayout")[0].child("com.ss.android.ugc.aweme:id/ebd").click()
sleep(1)
poco("android:id/content").child("android.widget.FrameLayout").offspring("com.ss.android.ugc.aweme:id/eo7").child("android.widget.LinearLayout").offspring("android.support.v7.widget.RecyclerView").child("android.widget.LinearLayout").offspring("com.ss.android.ugc.aweme:id/b8l").child("android.widget.ImageView")[0].click()
sleep(1)
poco(desc="视频1").click()
touch(Template(r"tpl1576112030695.png", record_pos=(0.435, 0.33), resolution=(810, 1440)))
sleep(2)
for n in range(50):
    comments = poco("com.ss.android.ugc.aweme:id/at0").offspring("android.widget.LinearLayout").offspring("com.ss.android.ugc.aweme:id/cto").child("com.ss.android.ugc.aweme:id/a22")
    for comment in comments:
        try:
            content = comment.offspring("com.ss.android.ugc.aweme:id/a2g").get_text()
            with open(r"C:\\Users\\12064\\Desktop\\蔡昀恩1.csv", "a+", encoding="utf8", errors="ignore") as f:
                f.write(content + '\n')
                f.close()
        except PocoNoSuchNodeException:
            pass
    poco("com.ss.android.ugc.aweme:id/cto").swipe([-0.1143, -0.4767])
    sleep(1) 
touch(Template(r"tpl1576909650261.png", record_pos=(0.447, -0.195), resolution=(810, 1440)))
sleep(2)
touch(Template(r"tpl1576908931930.png", record_pos=(-0.451, -0.777), resolution=(810, 1440)))
sleep(2)
poco(desc="视频2").click()
touch(Template(r"tpl1576112030695.png", record_pos=(0.435, 0.33), resolution=(810, 1440)))
sleep(2)
for n in range(50):
    comments = poco("com.ss.android.ugc.aweme:id/at0").offspring("android.widget.LinearLayout").offspring("com.ss.android.ugc.aweme:id/cto").child("com.ss.android.ugc.aweme:id/a22")
    for comment in comments:
        try:
            content = comment.offspring("com.ss.android.ugc.aweme:id/a2g").get_text()
            with open(r"C:\\Users\\12064\\Desktop\\蔡昀恩2.csv", "a+", encoding="utf8", errors="ignore") as f:
                f.write(content + '\n')
                f.close()
        except PocoNoSuchNodeException:
            pass
    poco("com.ss.android.ugc.aweme:id/cto").swipe([-0.1143, -0.4767])
    sleep(1) 
touch(Template(r"tpl1576909650261.png", record_pos=(0.447, -0.195), resolution=(810, 1440)))
sleep(2)
touch(Template(r"tpl1576908931930.png", record_pos=(-0.451, -0.777), resolution=(810, 1440)))
sleep(2)
poco(desc="视频3").click()
touch(Template(r"tpl1576112030695.png", record_pos=(0.435, 0.33), resolution=(810, 1440)))
sleep(2)
for n in range(50):
    comments = poco("com.ss.android.ugc.aweme:id/at0").offspring("android.widget.LinearLayout").offspring("com.ss.android.ugc.aweme:id/cto").child("com.ss.android.ugc.aweme:id/a22")
    for comment in comments:
        try:
            content = comment.offspring("com.ss.android.ugc.aweme:id/a2g").get_text()
            with open(r"C:\\Users\\12064\\Desktop\\蔡昀恩3.csv", "a+", encoding="utf8", errors="ignore") as f:
                f.write(content + '\n')
                f.close()
        except PocoNoSuchNodeException:
            pass
    poco("com.ss.android.ugc.aweme:id/cto").swipe([-0.1143, -0.4767])
    sleep(1)