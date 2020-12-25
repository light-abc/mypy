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


class BankCardData(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0x3e24e573``

    Parameters:
        title: ``str``
        open_urls: List of :obj:`BankCardOpenUrl <pyrogram.api.types.BankCardOpenUrl>`

    See Also:
        This object can be returned by :obj:`payments.GetBankCardData <pyrogram.api.functions.payments.GetBankCardData>`.
    """

    __slots__ = ["title", "open_urls"]

    ID = 0x3e24e573
    QUALNAME = "types.payments.BankCardData"

    def __init__(self, *, title: str, open_urls: list):
        self.title = title  # string
        self.open_urls = open_urls  # Vector<BankCardOpenUrl>

    @staticmethod
    def read(b: BytesIO, *args) -> "BankCardData":
        # No flags
        
        title = String.read(b)
        
        open_urls = TLObject.read(b)
        
        return BankCardData(title=title, open_urls=open_urls)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.title))
        
        b.write(Vector(self.open_urls))
        
        return b.getvalue()
