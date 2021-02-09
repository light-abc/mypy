# encoding: utf-8
import requests

# 检查是否连接入校园网
def checkinternet():
    url = 'xxxxxxxxxxxxxxxxxxxxxx'  #校园网登录的地址，用来测试是否连接校园网
    try:
        code = requests.get(url, timeout=5).status_code
        if code != 200:
            print('没有网络哦~')
            return 0
        elif code == 200:
            return 1
        else:
            return 2
    except:
        return 2


def login(username, password):
    url = 'xxxxxxxxxxxxxxxxxx' # 校园网表单提交url
    postdata={
        'action': 'login',
        'ac_id': 1,
        'user_ip':'',
        'nas_ip':'',
        'user_mac':'',
        'username': username,
        'password': password,
        'save_me': '0',
        'ajax': 1
    }
    res = requests.post(url, data=postdata)
    res.encoding = res.apparent_encoding
    res = res.text
    if 'login ok' in res:  # 如果存在该字段
        res = "登录成功！"
        return res
    if '5分钟' in res:  # 多次错误提交可能会导致账户锁定5分钟
        print("登录失败：")
        return res
    if 'E2620' in res:   # 此处是账号已经在别的设备登录的情况，先注销然后再次登录
        logout(url, username, password)
        return login(username, password)
    return res

# 退出当前账号的登录
def logout(url, username, password):
    logout_data = {
        'action': 'logout',
        'username': username,
        'password': password,
        'ajax': 1
    }
    res1 = requests.post(url, data=logout_data)
    res1.encoding = res1.apparent_encoding
    res1 = res1.text
    print("账户已退出！")


if __name__ == '__main__':
    status = checkinternet()
    if status == 0:
        txt = login(xxxxx, xxxxxxxx) # 输入账号密码
        print(txt)
    elif status == 1:
        print("有网络！")
        txt = login(xxxxxxx, xxxxxxx)
        print(txt)
    else:
        print("未知结果！")