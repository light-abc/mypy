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


class GetWallPaper(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0xfc8ddbea``

    Parameters:
        wallpaper: Either :obj:`InputWallPaper <pyrogram.api.types.InputWallPaper>`, :obj:`InputWallPaperSlug <pyrogram.api.types.InputWallPaperSlug>` or :obj:`InputWallPaperNoFile <pyrogram.api.types.InputWallPaperNoFile>`

    Returns:
        Either :obj:`WallPaper <pyrogram.api.types.WallPaper>` or :obj:`WallPaperNoFile <pyrogram.api.types.WallPaperNoFile>`
    """

    __slots__ = ["wallpaper"]

    ID = 0xfc8ddbea
    QUALNAME = "functions.account.GetWallPaper"

    def __init__(self, *, wallpaper):
        self.wallpaper = wallpaper  # InputWallPaper

    @staticmethod
    def read(b: BytesIO, *args) -> "GetWallPaper":
        # No flags
        
        wallpaper = TLObject.read(b)
        
        return GetWallPaper(wallpaper=wallpaper)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.wallpaper.write())
        
        return b.getvalue()
