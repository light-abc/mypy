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


class WebPageNotModified(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0x7311ca11``

    Parameters:
        cached_page_views (optional): ``int`` ``32-bit``

    See Also:
        This object can be returned by :obj:`messages.GetWebPage <pyrogram.api.functions.messages.GetWebPage>`.
    """

    __slots__ = ["cached_page_views"]

    ID = 0x7311ca11
    QUALNAME = "types.WebPageNotModified"

    def __init__(self, *, cached_page_views: int = None):
        self.cached_page_views = cached_page_views  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args) -> "WebPageNotModified":
        flags = Int.read(b)
        
        cached_page_views = Int.read(b) if flags & (1 << 0) else None
        return WebPageNotModified(cached_page_views=cached_page_views)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.cached_page_views is not None else 0
        b.write(Int(flags))
        
        if self.cached_page_views is not None:
            b.write(Int(self.cached_page_views))
        
        return b.getvalue()
