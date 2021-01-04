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
    # assert page.url == "https://account.xiaomi.com/pass/serviceLogin?callback=http://order.mi.com/login/callback?followup=https%3A%2F%2Fwww.mi.com%2F&sign=NzY3MDk1YzczNmUwMGM4ODAxOWE0NjRiNTU5ZGQyMzFhYjFmOGU0Nw,,&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180"

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

    # Click div[id="J_navMenu"] img[alt="小米11"]
    with page.expect_popup() as popup_info:
        page.click("div[id=\"J_navMenu\"] img[alt=\"小米11\"]")
    page1 = popup_info.value

    # Click text="立即购买"
    with page1.expect_popup() as popup_info:
        page1.click("text=\"立即购买\"")
    page2 = popup_info.value

    # Click text="12GB+256GB"
    page2.click("text=\"12GB+256GB\"")

    # Click text="雷军签名版"
    page2.click("text=\"雷军签名版\"")

    # Click text="套装版"
    page2.click("text=\"套装版\"")

    # Click text="加入购物车"
    page2.click("text=\"加入购物车\"")

    # Click //em
    page.click("//em")
    # assert page.url == "https://www.mi.com/buy/cart"
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)