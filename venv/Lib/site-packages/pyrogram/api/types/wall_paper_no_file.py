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


class WallPaperNoFile(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0x8af40b25``

    Parameters:
        default (optional): ``bool``
        dark (optional): ``bool``
        settings (optional): :obj:`WallPaperSettings <pyrogram.api.types.WallPaperSettings>`

    See Also:
        This object can be returned by :obj:`account.GetWallPaper <pyrogram.api.functions.account.GetWallPaper>`, :obj:`account.UploadWallPaper <pyrogram.api.functions.account.UploadWallPaper>` and :obj:`account.GetMultiWallPapers <pyrogram.api.functions.account.GetMultiWallPapers>`.
    """

    __slots__ = ["default", "dark", "settings"]

    ID = 0x8af40b25
    QUALNAME = "types.WallPaperNoFile"

    def __init__(self, *, default: bool = None, dark: bool = None, settings=None):
        self.default = default  # flags.1?true
        self.dark = dark  # flags.4?true
        self.settings = settings  # flags.2?WallPaperSettings

    @staticmethod
    def read(b: BytesIO, *args) -> "WallPaperNoFile":
        flags = Int.read(b)
        
        default = True if flags & (1 << 1) else False
        dark = True if flags & (1 << 4) else False
        settings = TLObject.read(b) if flags & (1 << 2) else None
        
        return WallPaperNoFile(default=default, dark=dark, settings=settings)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.default is not None else 0
        flags |= (1 << 4) if self.dark is not None else 0
        flags |= (1 << 2) if self.settings is not None else 0
        b.write(Int(flags))
        
        if self.settings is not None:
            b.write(self.settings.write())
        
        return b.getvalue()
