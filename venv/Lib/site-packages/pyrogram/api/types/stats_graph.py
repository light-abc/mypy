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


class StatsGraph(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0x8ea464b6``

    Parameters:
        json: :obj:`DataJSON <pyrogram.api.types.DataJSON>`
        zoom_token (optional): ``str``

    See Also:
        This object can be returned by :obj:`stats.LoadAsyncGraph <pyrogram.api.functions.stats.LoadAsyncGraph>`.
    """

    __slots__ = ["json", "zoom_token"]

    ID = 0x8ea464b6
    QUALNAME = "types.StatsGraph"

    def __init__(self, *, json, zoom_token: str = None):
        self.json = json  # DataJSON
        self.zoom_token = zoom_token  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args) -> "StatsGraph":
        flags = Int.read(b)
        
        json = TLObject.read(b)
        
        zoom_token = String.read(b) if flags & (1 << 0) else None
        return StatsGraph(json=json, zoom_token=zoom_token)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.zoom_token is not None else 0
        b.write(Int(flags))
        
        b.write(self.json.write())
        
        if self.zoom_token is not None:
            b.write(String(self.zoom_token))
        
        return b.getvalue()
