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


class GetBroadcastStats(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0xe6300dba``

    Parameters:
        channel: Either :obj:`InputChannelEmpty <pyrogram.api.types.InputChannelEmpty>`, :obj:`InputChannel <pyrogram.api.types.InputChannel>` or :obj:`InputChannelFromMessage <pyrogram.api.types.InputChannelFromMessage>`
        tz_offset: ``int`` ``32-bit``
        dark (optional): ``bool``

    Returns:
        :obj:`stats.BroadcastStats <pyrogram.api.types.stats.BroadcastStats>`
    """

    __slots__ = ["channel", "tz_offset", "dark"]

    ID = 0xe6300dba
    QUALNAME = "functions.stats.GetBroadcastStats"

    def __init__(self, *, channel, tz_offset: int, dark: bool = None):
        self.dark = dark  # flags.0?true
        self.channel = channel  # InputChannel
        self.tz_offset = tz_offset  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetBroadcastStats":
        flags = Int.read(b)
        
        dark = True if flags & (1 << 0) else False
        channel = TLObject.read(b)
        
        tz_offset = Int.read(b)
        
        return GetBroadcastStats(channel=channel, tz_offset=tz_offset, dark=dark)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.dark is not None else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(Int(self.tz_offset))
        
        return b.getvalue()
