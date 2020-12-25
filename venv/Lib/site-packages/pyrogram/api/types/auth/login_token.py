# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.api.core import *


class LoginToken(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0x629f1980``

    Parameters:
        expires: ``int`` ``32-bit``
        token: ``bytes``

    See Also:
        This object can be returned by :obj:`auth.ExportLoginToken <pyrogram.api.functions.auth.ExportLoginToken>` and :obj:`auth.ImportLoginToken <pyrogram.api.functions.auth.ImportLoginToken>`.
    """

    __slots__ = ["expires", "token"]

    ID = 0x629f1980
    QUALNAME = "types.auth.LoginToken"

    def __init__(self, *, expires: int, token: bytes):
        self.expires = expires  # int
        self.token = token  # bytes

    @staticmethod
    def read(b: BytesIO, *args) -> "LoginToken":
        # No flags
        
        expires = Int.read(b)
        
        token = Bytes.read(b)
        
        return LoginToken(expires=expires, token=token)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.expires))
        
        b.write(Bytes(self.token))
        
        return b.getvalue()
