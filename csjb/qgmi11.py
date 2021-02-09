from playwright import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    # Go to https://www.mi.com/
    page.goto("https://www.mi.com/")

    # Click text="登录"
    page.click("text=\"登录\"")

    # Click text="同意"
    page.click("text=\"同意\"")
    # assert page.url == "https://account.xiaomi.com/pass/serviceLogin?callback=http%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252F%26sign%3DNzY3MDk1YzczNmUwMGM4ODAxOWE0NjRiNTU5ZGQyMzFhYjFmOGU0Nw%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180"

    # Click input[name="user"]
    page.click("input[name=\"user\"]")

    # Fill input[name="user"]
    page.fill("input[name=\"user\"]", "18205087471")

    # Press Tab
    page.press("input[name=\"user\"]", "Tab")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "hll1999628")

    # Press Enter
    # with page.expect_navigation(url="https://www.mi.com/"):
    with page.expect_navigation():
        page.press("input[name=\"password\"]", "Enter")

    # Click //a[normalize-space(.)='小米11 骁龙888 | 2K四曲面屏3999元起']/div/img[normalize-space(@alt)='小米11']
    # with page.expect_popup() as popup_info:
    #     page.click("//a[normalize-space(.)='小米11 骁龙888 | 2K四曲面屏3999元起']/div/img[normalize-space(@alt)='小米11']")
    # page1 = popup_info.value

    # Click text="立即购买"
    with page1.expect_popup() as popup_info:
        page1.click("text=\"立即购买\"")
    page2 = popup_info.value

    # Click text="12GB+256GB"
    page2.click("text=\"12GB+256GB\"")

    # Click text="雷军签名版"
    page2.click("text=\"雷军签名版\"")

    # Click text="敬请期待"
    page2.click("text=\"立即抢购\"")

    # Click text="套装版（赠充电器）"
    page2.click("text=\"套装版（赠充电器）\"")

    # Click text="立即预约"
    page2.click("text=\"立即抢购\"")

    # Close page
    page2.close()

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
