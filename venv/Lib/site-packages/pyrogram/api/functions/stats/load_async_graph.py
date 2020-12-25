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


class LoadAsyncGraph(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0x621d5fa0``

    Parameters:
        token: ``str``
        x (optional): ``int`` ``64-bit``

    Returns:
        Either :obj:`StatsGraphAsync <pyrogram.api.types.StatsGraphAsync>`, :obj:`StatsGraphError <pyrogram.api.types.StatsGraphError>` or :obj:`StatsGraph <pyrogram.api.types.StatsGraph>`
    """

    __slots__ = ["token", "x"]

    ID = 0x621d5fa0
    QUALNAME = "functions.stats.LoadAsyncGraph"

    def __init__(self, *, token: str, x: int = None):
        self.token = token  # string
        self.x = x  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args) -> "LoadAsyncGraph":
        flags = Int.read(b)
        
        token = String.read(b)
        
        x = Long.read(b) if flags & (1 << 0) else None
        return LoadAsyncGraph(token=token, x=x)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.x is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.token))
        
        if self.x is not None:
            b.write(Long(self.x))
        
        return b.getvalue()
