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


class GetLocated(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0xd348bc44``

    Parameters:
        geo_point: Either :obj:`InputGeoPointEmpty <pyrogram.api.types.InputGeoPointEmpty>` or :obj:`InputGeoPoint <pyrogram.api.types.InputGeoPoint>`
        background (optional): ``bool``
        self_expires (optional): ``int`` ``32-bit``

    Returns:
        Either :obj:`UpdatesTooLong <pyrogram.api.types.UpdatesTooLong>`, :obj:`UpdateShortMessage <pyrogram.api.types.UpdateShortMessage>`, :obj:`UpdateShortChatMessage <pyrogram.api.types.UpdateShortChatMessage>`, :obj:`UpdateShort <pyrogram.api.types.UpdateShort>`, :obj:`UpdatesCombined <pyrogram.api.types.UpdatesCombined>`, :obj:`Update <pyrogram.api.types.Update>` or :obj:`UpdateShortSentMessage <pyrogram.api.types.UpdateShortSentMessage>`
    """

    __slots__ = ["geo_point", "background", "self_expires"]

    ID = 0xd348bc44
    QUALNAME = "functions.contacts.GetLocated"

    def __init__(self, *, geo_point, background: bool = None, self_expires: int = None):
        self.background = background  # flags.1?true
        self.geo_point = geo_point  # InputGeoPoint
        self.self_expires = self_expires  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetLocated":
        flags = Int.read(b)
        
        background = True if flags & (1 << 1) else False
        geo_point = TLObject.read(b)
        
        self_expires = Int.read(b) if flags & (1 << 0) else None
        return GetLocated(geo_point=geo_point, background=background, self_expires=self_expires)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.background is not None else 0
        flags |= (1 << 0) if self.self_expires is not None else 0
        b.write(Int(flags))
        
        b.write(self.geo_point.write())
        
        if self.self_expires is not None:
            b.write(Int(self.self_expires))
        
        return b.getvalue()
