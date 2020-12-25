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


class ThemeSettings(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0x9c14984a``

    Parameters:
        base_theme: Either :obj:`BaseThemeClassic <pyrogram.api.types.BaseThemeClassic>`, :obj:`BaseThemeDay <pyrogram.api.types.BaseThemeDay>`, :obj:`BaseThemeNight <pyrogram.api.types.BaseThemeNight>`, :obj:`BaseThemeTinted <pyrogram.api.types.BaseThemeTinted>` or :obj:`BaseThemeArctic <pyrogram.api.types.BaseThemeArctic>`
        accent_color: ``int`` ``32-bit``
        message_top_color (optional): ``int`` ``32-bit``
        message_bottom_color (optional): ``int`` ``32-bit``
        wallpaper (optional): Either :obj:`WallPaper <pyrogram.api.types.WallPaper>` or :obj:`WallPaperNoFile <pyrogram.api.types.WallPaperNoFile>`
    """

    __slots__ = ["base_theme", "accent_color", "message_top_color", "message_bottom_color", "wallpaper"]

    ID = 0x9c14984a
    QUALNAME = "types.ThemeSettings"

    def __init__(self, *, base_theme, accent_color: int, message_top_color: int = None, message_bottom_color: int = None, wallpaper=None):
        self.base_theme = base_theme  # BaseTheme
        self.accent_color = accent_color  # int
        self.message_top_color = message_top_color  # flags.0?int
        self.message_bottom_color = message_bottom_color  # flags.0?int
        self.wallpaper = wallpaper  # flags.1?WallPaper

    @staticmethod
    def read(b: BytesIO, *args) -> "ThemeSettings":
        flags = Int.read(b)
        
        base_theme = TLObject.read(b)
        
        accent_color = Int.read(b)
        
        message_top_color = Int.read(b) if flags & (1 << 0) else None
        message_bottom_color = Int.read(b) if flags & (1 << 0) else None
        wallpaper = TLObject.read(b) if flags & (1 << 1) else None
        
        return ThemeSettings(base_theme=base_theme, accent_color=accent_color, message_top_color=message_top_color, message_bottom_color=message_bottom_color, wallpaper=wallpaper)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.message_top_color is not None else 0
        flags |= (1 << 0) if self.message_bottom_color is not None else 0
        flags |= (1 << 1) if self.wallpaper is not None else 0
        b.write(Int(flags))
        
        b.write(self.base_theme.write())
        
        b.write(Int(self.accent_color))
        
        if self.message_top_color is not None:
            b.write(Int(self.message_top_color))
        
        if self.message_bottom_color is not None:
            b.write(Int(self.message_bottom_color))
        
        if self.wallpaper is not None:
            b.write(self.wallpaper.write())
        
        return b.getvalue()
