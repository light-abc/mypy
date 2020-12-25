import time

def i_want_to_sleep(delay):
    assert (isinstance(delay, (int, float))), '函数参数必须为整数或浮点数'
    print('开始睡觉')
    time.sleep(delay)
    print('睡醒了')

i_want_to_sleep(3.1)
i_want_to_sleep(2)