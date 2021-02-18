import uiautomator2 as u2
import time
import random
# d = u2.connect()  # 有线连接，手机需要插电脑上
d = u2.connect("192.168.0.108") #通过无线连接，电脑和手机需要在同一个局域网内，并且需要先用有线的方式做过初始化


# d.app_stop("com.eg.android.AlipayGphone")

print("打开支付宝")
d.app_start("com.eg.android.AlipayGphone")
time.sleep(2) ## 休眠2s等待支付宝完全启动

print("打开蚂蚁森林，等待5s……")
d(text="蚂蚁森林").click()
time.sleep(5) ## 我手机比较卡，进入蚂蚁森林后还需要几秒钟才能完全加载完

def collectEnergy(cnt):
    print("开始第%d次偷能量！" % cnt)

    # 开始扫描点击有能力出现的区域
    for x in range(150,1000,150):
        for y in range(600,900,150):
            d.long_click(x + random.randint(10,20), y + random.randint(10,20), 0.1)
            time.sleep(0.01)
            if cnt != 1:
                d.click(536,1816)

cnt = 1
while True:
    collectEnergy(cnt)
    a = d.xpath("//*[@resource-id='J_tree_dialog_wrap']").get().bounds
    d.click(1000, a[3]-80) # 找能量按钮的坐标

    ## 如果页面出现了“返回我的森林”说明已经没有能量可偷了，结束
    if d.xpath('//*[@text="返回我的森林"]').click_exists(timeout=2.0):
        break
    cnt += 1
print("###结束###")
# d.app_stop("com.eg.android.AlipayGphone") # 退出支付宝