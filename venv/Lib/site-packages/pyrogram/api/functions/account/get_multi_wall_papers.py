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


class GetMultiWallPapers(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0x65ad71dc``

    Parameters:
        wallpapers: List of either :obj:`InputWallPaper <pyrogram.api.types.InputWallPaper>`, :obj:`InputWallPaperSlug <pyrogram.api.types.InputWallPaperSlug>` or :obj:`InputWallPaperNoFile <pyrogram.api.types.InputWallPaperNoFile>`

    Returns:
        List of either :obj:`WallPaper <pyrogram.api.types.WallPaper>` or :obj:`WallPaperNoFile <pyrogram.api.types.WallPaperNoFile>`
    """

    __slots__ = ["wallpapers"]

    ID = 0x65ad71dc
    QUALNAME = "functions.account.GetMultiWallPapers"

    def __init__(self, *, wallpapers: list):
        self.wallpapers = wallpapers  # Vector<InputWallPaper>

    @staticmethod
    def read(b: BytesIO, *args) -> "GetMultiWallPapers":
        # No flags
        
        wallpapers = TLObject.read(b)
        
        return GetMultiWallPapers(wallpapers=wallpapers)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.wallpapers))
        
        return b.getvalue()
