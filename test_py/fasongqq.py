import win32

class sendMsg():
    def __init__(self,receiver,msg):
        self.receiver=receiver
        self.msg=msg
        self.setText()
    #设置剪贴版内容
    def setText(self):
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, self.msg)
        w.CloseClipboard()
    #发送消息
    def sendmsg(self):
        qq=win32gui.FindWindow(None,self.receiver)
        win32gui.SendMessage(qq,win32con.WM_PASTE , 0, 0) #win32on 见site-packages\win32\lib\win32con.py,有的博文里出现的770对用的就是win32con.WM_PASTE
        win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)


if __name__ == '__main__':
    receiver='哥'
    msg="测试"
    qq=sendMsg(receiver,msg)
    qq.sendmsg()