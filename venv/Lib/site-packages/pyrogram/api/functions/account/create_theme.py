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


class CreateTheme(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0x8432c21f``

    Parameters:
        slug: ``str``
        title: ``str``
        document (optional): Either :obj:`InputDocumentEmpty <pyrogram.api.types.InputDocumentEmpty>` or :obj:`InputDocument <pyrogram.api.types.InputDocument>`
        settings (optional): :obj:`InputThemeSettings <pyrogram.api.types.InputThemeSettings>`

    Returns:
        :obj:`Theme <pyrogram.api.types.Theme>`
    """

    __slots__ = ["slug", "title", "document", "settings"]

    ID = 0x8432c21f
    QUALNAME = "functions.account.CreateTheme"

    def __init__(self, *, slug: str, title: str, document=None, settings=None):
        self.slug = slug  # string
        self.title = title  # string
        self.document = document  # flags.2?InputDocument
        self.settings = settings  # flags.3?InputThemeSettings

    @staticmethod
    def read(b: BytesIO, *args) -> "CreateTheme":
        flags = Int.read(b)
        
        slug = String.read(b)
        
        title = String.read(b)
        
        document = TLObject.read(b) if flags & (1 << 2) else None
        
        settings = TLObject.read(b) if flags & (1 << 3) else None
        
        return CreateTheme(slug=slug, title=title, document=document, settings=settings)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.document is not None else 0
        flags |= (1 << 3) if self.settings is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.slug))
        
        b.write(String(self.title))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.settings is not None:
            b.write(self.settings.write())
        
        return b.getvalue()
