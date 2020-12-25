import base64, os
from Crypto.Hash import SHA256
from Crypto.Cipher import ARC4
from base64 import *

import re

class xshell_secret():

    sid = [i.split(" ") for i in os.popen(r'whoami /user').read().split('\n') if
           re.findall(r"[0-9]+", str(os.path.join(os.path.expanduser("~"))))[0] in i][0][-1]

    # 解密
    def decrypt_string(self, lpassowrd):
        v1 = base64.b64decode(lpassowrd)
        v3 = ARC4.new(SHA256.new(self.sid.encode('ascii')).digest()).decrypt(v1[:len(v1) - 0x20])
        if SHA256.new(v3).digest() == v1[-32:]:
            return v3.decode('ascii')
        else:
            return None
    # 加密
    def encrypt_string(self, spassowrd):
        rawPass = bytes(spassowrd, encoding='utf8')
        sid = bytes(self.sid, encoding='utf8')
        cipher = ARC4.new(SHA256.new(sid).digest())
        checksum = SHA256.new(rawPass).digest()
        ciphertext = cipher.encrypt(rawPass)
        return b64encode(ciphertext + checksum).decode()

