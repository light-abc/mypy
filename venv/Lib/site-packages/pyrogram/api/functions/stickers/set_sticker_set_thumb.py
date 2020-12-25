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


class SetStickerSetThumb(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0x9a364e30``

    Parameters:
        stickerset: Either :obj:`InputStickerSetEmpty <pyrogram.api.types.InputStickerSetEmpty>`, :obj:`InputStickerSetID <pyrogram.api.types.InputStickerSetID>`, :obj:`InputStickerSetShortName <pyrogram.api.types.InputStickerSetShortName>`, :obj:`InputStickerSetAnimatedEmoji <pyrogram.api.types.InputStickerSetAnimatedEmoji>` or :obj:`InputStickerSetDice <pyrogram.api.types.InputStickerSetDice>`
        thumb: Either :obj:`InputDocumentEmpty <pyrogram.api.types.InputDocumentEmpty>` or :obj:`InputDocument <pyrogram.api.types.InputDocument>`

    Returns:
        :obj:`messages.StickerSet <pyrogram.api.types.messages.StickerSet>`
    """

    __slots__ = ["stickerset", "thumb"]

    ID = 0x9a364e30
    QUALNAME = "functions.stickers.SetStickerSetThumb"

    def __init__(self, *, stickerset, thumb):
        self.stickerset = stickerset  # InputStickerSet
        self.thumb = thumb  # InputDocument

    @staticmethod
    def read(b: BytesIO, *args) -> "SetStickerSetThumb":
        # No flags
        
        stickerset = TLObject.read(b)
        
        thumb = TLObject.read(b)
        
        return SetStickerSetThumb(stickerset=stickerset, thumb=thumb)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.stickerset.write())
        
        b.write(self.thumb.write())
        
        return b.getvalue()
