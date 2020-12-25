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


class ToggleStickerSets(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0xb5052fea``

    Parameters:
        stickersets: List of either :obj:`InputStickerSetEmpty <pyrogram.api.types.InputStickerSetEmpty>`, :obj:`InputStickerSetID <pyrogram.api.types.InputStickerSetID>`, :obj:`InputStickerSetShortName <pyrogram.api.types.InputStickerSetShortName>`, :obj:`InputStickerSetAnimatedEmoji <pyrogram.api.types.InputStickerSetAnimatedEmoji>` or :obj:`InputStickerSetDice <pyrogram.api.types.InputStickerSetDice>`
        uninstall (optional): ``bool``
        archive (optional): ``bool``
        unarchive (optional): ``bool``

    Returns:
        ``bool``
    """

    __slots__ = ["stickersets", "uninstall", "archive", "unarchive"]

    ID = 0xb5052fea
    QUALNAME = "functions.messages.ToggleStickerSets"

    def __init__(self, *, stickersets: list, uninstall: bool = None, archive: bool = None, unarchive: bool = None):
        self.uninstall = uninstall  # flags.0?true
        self.archive = archive  # flags.1?true
        self.unarchive = unarchive  # flags.2?true
        self.stickersets = stickersets  # Vector<InputStickerSet>

    @staticmethod
    def read(b: BytesIO, *args) -> "ToggleStickerSets":
        flags = Int.read(b)
        
        uninstall = True if flags & (1 << 0) else False
        archive = True if flags & (1 << 1) else False
        unarchive = True if flags & (1 << 2) else False
        stickersets = TLObject.read(b)
        
        return ToggleStickerSets(stickersets=stickersets, uninstall=uninstall, archive=archive, unarchive=unarchive)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.uninstall is not None else 0
        flags |= (1 << 1) if self.archive is not None else 0
        flags |= (1 << 2) if self.unarchive is not None else 0
        b.write(Int(flags))
        
        b.write(Vector(self.stickersets))
        
        return b.getvalue()
