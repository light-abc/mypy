from selenium import webdriver
import datetime

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

browser = webdriver.Chrome()

browser.get("https://mobile.yangkeduo.com/goods1.html?goods_id=176997495583&page_from=0&pxq_secret_key=G64Y4QMUV3DS5T233AYXHTX5D5UJMC2YAE2C74Z4GUNDKN55OLGQ&share_uin=434MBTU62HYTZVGKVLT32PTW4M_GEXDA&_wv=1&refer_share_id=2bfaa28a072a45f49d77053cda8027f0&refer_share_uid=5963273086&refer_share_channel=qq&refer_share_form=card&_wvx=10")

browser.find_element_by_link_text("G64Y4QMUV3DS5T233AYXHTX5D5UJMC2YAE2C74Z4GUNDKN55OLGQ").click()

# def login():
#     # 打开淘宝首页，通过扫码登录
#     browser.get("https://www.taobao.com")
#     time.sleep(3)
#     if browser.find_element_by_link_text("亲，请登录"):
#         browser.find_element_by_link_text("亲，请登录").click()
#         print(f"请尽快扫码登录")
#         time.sleep(10)
#
# def picking(method):
#     # 打开购物车列表页面
#     browser.get("https://cart.taobao.com/cart.htm")
#     time.sleep(3)
#
#
#     # 是否全选购物车
#     if method == 0:
#         while True:
#             try:
#                 if browser.find_element_by_id("J_SelectAll1"):
#                     browser.find_element_by_id("J_SelectAll1").click()
#                     break
#             except:
#                 print(f"找不到购买按钮")
#     else:
#         print(f"请手动勾选需要购买的商品")
#         time.sleep(5)
#
# def buy(times):
#     while True:
#         now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
#         # 对比时间，时间到的话就点击结算
#         if now > times:
#             # 点击结算按钮
#             while True:
#                 try:
#                     if browser.find_element_by_link_text("结 算"):
#                         browser.find_element_by_link_text("结 算").click()
#                         print(f"结算成功，准备提交订单")
#                         break
#                 except:
#                     pass
#             # 点击提交订单按钮
#             while True:
#                 try:
#                     if browser.find_element_by_link_text('提交订单'):
#                         browser.find_element_by_link_text('提交订单').click()
#                         print(f"抢购成功，请尽快付款")
#                 except:
#                     print(f"再次尝试提交订单")
#             time.sleep(0.01)
