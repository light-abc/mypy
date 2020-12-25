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


class MessageMediaDice(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0x3f7ee58b``

    Parameters:
        value: ``int`` ``32-bit``
        emoticon: ``str``

    See Also:
        This object can be returned by :obj:`messages.GetWebPagePreview <pyrogram.api.functions.messages.GetWebPagePreview>` and :obj:`messages.UploadMedia <pyrogram.api.functions.messages.UploadMedia>`.
    """

    __slots__ = ["value", "emoticon"]

    ID = 0x3f7ee58b
    QUALNAME = "types.MessageMediaDice"

    def __init__(self, *, value: int, emoticon: str):
        self.value = value  # int
        self.emoticon = emoticon  # string

    @staticmethod
    def read(b: BytesIO, *args) -> "MessageMediaDice":
        # No flags
        
        value = Int.read(b)
        
        emoticon = String.read(b)
        
        return MessageMediaDice(value=value, emoticon=emoticon)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.value))
        
        b.write(String(self.emoticon))
        
        return b.getvalue()
