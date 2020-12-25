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


class CreateStickerSet(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0xf1036780``

    Parameters:
        user_id: Either :obj:`InputUserEmpty <pyrogram.api.types.InputUserEmpty>`, :obj:`InputUserSelf <pyrogram.api.types.InputUserSelf>`, :obj:`InputUser <pyrogram.api.types.InputUser>` or :obj:`InputUserFromMessage <pyrogram.api.types.InputUserFromMessage>`
        title: ``str``
        short_name: ``str``
        stickers: List of :obj:`InputStickerSetItem <pyrogram.api.types.InputStickerSetItem>`
        masks (optional): ``bool``
        animated (optional): ``bool``
        thumb (optional): Either :obj:`InputDocumentEmpty <pyrogram.api.types.InputDocumentEmpty>` or :obj:`InputDocument <pyrogram.api.types.InputDocument>`

    Returns:
        :obj:`messages.StickerSet <pyrogram.api.types.messages.StickerSet>`
    """

    __slots__ = ["user_id", "title", "short_name", "stickers", "masks", "animated", "thumb"]

    ID = 0xf1036780
    QUALNAME = "functions.stickers.CreateStickerSet"

    def __init__(self, *, user_id, title: str, short_name: str, stickers: list, masks: bool = None, animated: bool = None, thumb=None):
        self.masks = masks  # flags.0?true
        self.animated = animated  # flags.1?true
        self.user_id = user_id  # InputUser
        self.title = title  # string
        self.short_name = short_name  # string
        self.thumb = thumb  # flags.2?InputDocument
        self.stickers = stickers  # Vector<InputStickerSetItem>

    @staticmethod
    def read(b: BytesIO, *args) -> "CreateStickerSet":
        flags = Int.read(b)
        
        masks = True if flags & (1 << 0) else False
        animated = True if flags & (1 << 1) else False
        user_id = TLObject.read(b)
        
        title = String.read(b)
        
        short_name = String.read(b)
        
        thumb = TLObject.read(b) if flags & (1 << 2) else None
        
        stickers = TLObject.read(b)
        
        return CreateStickerSet(user_id=user_id, title=title, short_name=short_name, stickers=stickers, masks=masks, animated=animated, thumb=thumb)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.masks is not None else 0
        flags |= (1 << 1) if self.animated is not None else 0
        flags |= (1 << 2) if self.thumb is not None else 0
        b.write(Int(flags))
        
        b.write(self.user_id.write())
        
        b.write(String(self.title))
        
        b.write(String(self.short_name))
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        b.write(Vector(self.stickers))
        
        return b.getvalue()
