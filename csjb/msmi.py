from playwright import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    # Go to https://www.mi.com/
    page.goto("https://www.mi.com/")

    # Click //em
    page.click("//em")
    # assert page.url == "https://www.mi.com/buy/cart"

    # Click text="登录"
    page.click("text=\"登录\"")

    # Click text="同意"
    page.click("text=\"同意\"")
    # assert page.url == "https://account.xiaomi.com/pass/serviceLogin?callback=http%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252Fbuy%252Fcart%26sign%3DMTI1MTkyY2VkOGUxODVlZDM0YTViODMyNmU0ZTcxNDZiNGUzYmFlMw%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180"

    # Click input[name="user"]
    page.click("input[name=\"user\"]")

    # Click input[name="user"]
    page.click("input[name=\"user\"]")

    # Click input[name="user"]
    page.click("input[name=\"user\"]")

    # Click input[name="user"]
    page.click("input[name=\"user\"]")

    # Click div[id="J_panel"] >> text="小米网"
    page.frame(url="https://s1.mi.com/loginbanner.html").click("div[id=\"J_panel\"] >> text=\"小米网\"")
    # assert page.url == "https://www.mi.com/redmi10x-5G"

    # Go to https://account.xiaomi.com/pass/serviceLogin?callback=http%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252Fbuy%252Fcart%26sign%3DMTI1MTkyY2VkOGUxODVlZDM0YTViODMyNmU0ZTcxNDZiNGUzYmFlMw%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180
    page.goto("https://account.xiaomi.com/pass/serviceLogin?callback=http%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252Fbuy%252Fcart%26sign%3DMTI1MTkyY2VkOGUxODVlZDM0YTViODMyNmU0ZTcxNDZiNGUzYmFlMw%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180")

    # Click //div[4]/div[normalize-space(.)='获取验证码 使用安全控件 手机短信登录/注册 立即注册| 忘记密码？ 收不到验证码？ 其他方式登录']
    page.click("//div[4]/div[normalize-space(.)='获取验证码 使用安全控件 手机短信登录/注册 立即注册| 忘记密码？ 收不到验证码？ 其他方式登录']")

    # Click text="扫码登录"
    page.click("text=\"扫码登录\"")

    # Click text="帐号登录"
    page.click("text=\"帐号登录\"")

    # Click input[name="user"]
    page.click("input[name=\"user\"]")

    # Fill input[name="user"]
    page.fill("input[name=\"user\"]", "18205087471")

    # Press Enter
    page.press("input[name=\"user\"]", "Enter")

    # Press Tab
    page.press("input[name=\"user\"]", "Tab")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "hll1999628")

    # Click input[type="button"]
    # with page.expect_navigation(url="https://www.mi.com/buy/cart"):
    with page.expect_navigation():
        page.click("input[type=\"button\"]")

    # Click text="去结算"
    # with page.expect_navigation(url="https://www.mi.com/buy/checkout?r=20173.1609743803"):
    with page.expect_navigation():
        page.click("text=\"去结算\"")

    # Click text="商品及优惠券"
    page.click("text=\"商品及优惠券\"")

    # Click //div[starts-with(normalize-space(.), '选择该收货地址黄亮亮182****7471江苏 南京市 建邺区 爱达花园兰花园4幢21号101室收货地址黄亮亮182****7471江苏南京市建邺区南苑街道爱达')]
    page.click("//div[starts-with(normalize-space(.), '选择该收货地址黄亮亮182****7471江苏 南京市 建邺区 爱达花园兰花园4幢21号101室收货地址黄亮亮182****7471江苏南京市建邺区南苑街道爱达')]")

    # Click //a[normalize-space(.)='Mr_Sunny']
    with page.expect_popup() as popup_info:
        page.click("//a[normalize-space(.)='Mr_Sunny']")
    page1 = popup_info.value

    # Close page
    page.close()

    # Click text="购物车"
    page1.click("text=\"购物车\"")
    # assert page1.url == "https://www.mi.com/buy/cart"

    # Click text="去结算"
    page1.click("text=\"去结算\"")

    # Go to https://www.mi.com/buy/checkout?r=77262.1609743928
    page1.goto("https://www.mi.com/buy/checkout?r=77262.1609743928")

    # Click //div[normalize-space(.)='黄亮亮182****7471江苏南京市建邺区南苑街道爱达花园兰花园4幢21号101室修改']
    page1.click("//div[normalize-space(.)='黄亮亮182****7471江苏南京市建邺区南苑街道爱达花园兰花园4幢21号101室修改']")

    # Click text="立即下单"
    # with page1.expect_navigation(url="https://www.mi.com/buy/confirm?id=5210104249202106"):
    with page1.expect_navigation():
        page1.click("text=\"立即下单\"")

    # Click //div[2]/div/div[starts-with(normalize-space(.), '订单提交成功！去付款咯～请在47 小时 59 分内完成支付, 超时后将取消订单收货信息：黄亮亮 182****7471 江苏 南京市 建邺区 南苑街道 爱达花园')]
    page1.click("//div[2]/div/div[starts-with(normalize-space(.), '订单提交成功！去付款咯～请在47 小时 59 分内完成支付, 超时后将取消订单收货信息：黄亮亮 182****7471 江苏 南京市 建邺区 南苑街道 爱达花园')]")

    # Click //li[3]/img
    with page1.expect_popup() as popup_info:
        page1.click("//li[3]/img")
    page2 = popup_info.value

    # Click text=""
    page1.click("text=\"\"")

    # Click //img
    with page1.expect_popup() as popup_info:
        page1.click("//img")
    page3 = popup_info.value

    # Go to https://m.mipay.com/payFunc?safe=79679a35f3c643f086597c6ba343e065&outOrderId=5210104249202106&partnerId=1000000004&cUserId=yTjtutofy3eTmN-3KHkzfl-r3Uk#/
    page3.goto("https://m.mipay.com/payFunc?safe=79679a35f3c643f086597c6ba343e065&outOrderId=5210104249202106&partnerId=1000000004&cUserId=yTjtutofy3eTmN-3KHkzfl-r3Uk#/")

    # Go to https://m.mipay.com/payFunc?safe=79679a35f3c643f086597c6ba343e065&outOrderId=5210104249202106&partnerId=1000000004&cUserId=yTjtutofy3eTmN-3KHkzfl-r3Uk#/pay
    page3.goto("https://m.mipay.com/payFunc?safe=79679a35f3c643f086597c6ba343e065&outOrderId=5210104249202106&partnerId=1000000004&cUserId=yTjtutofy3eTmN-3KHkzfl-r3Uk#/pay")

    # Close page
    page2.close()

    # Click //button[normalize-space(.)='立即支付']
    page3.click("//button[normalize-space(.)='立即支付']")

    # Go to https://m.mipay.com/payFunc?safe=79679a35f3c643f086597c6ba343e065&outOrderId=5210104249202106&partnerId=1000000004&cUserId=yTjtutofy3eTmN-3KHkzfl-r3Uk#/pay/password/pay
    page3.goto("https://m.mipay.com/payFunc?safe=79679a35f3c643f086597c6ba343e065&outOrderId=5210104249202106&partnerId=1000000004&cUserId=yTjtutofy3eTmN-3KHkzfl-r3Uk#/pay/password/pay")

    # Click //div[normalize-space(.)='忘记密码?']/div[1]/div/div
    page3.click("//div[normalize-space(.)='忘记密码?']/div[1]/div/div")

    # Close page
    page3.close()

    # Close page
    page1.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)