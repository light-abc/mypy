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


class ExportLoginToken(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0xb1b41517``

    Parameters:
        api_id: ``int`` ``32-bit``
        api_hash: ``str``
        except_ids: List of ``int`` ``32-bit``

    Returns:
        Either :obj:`auth.LoginToken <pyrogram.api.types.auth.LoginToken>`, :obj:`auth.LoginTokenMigrateTo <pyrogram.api.types.auth.LoginTokenMigrateTo>` or :obj:`auth.LoginTokenSuccess <pyrogram.api.types.auth.LoginTokenSuccess>`
    """

    __slots__ = ["api_id", "api_hash", "except_ids"]

    ID = 0xb1b41517
    QUALNAME = "functions.auth.ExportLoginToken"

    def __init__(self, *, api_id: int, api_hash: str, except_ids: list):
        self.api_id = api_id  # int
        self.api_hash = api_hash  # string
        self.except_ids = except_ids  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args) -> "ExportLoginToken":
        # No flags
        
        api_id = Int.read(b)
        
        api_hash = String.read(b)
        
        except_ids = TLObject.read(b, Int)
        
        return ExportLoginToken(api_id=api_id, api_hash=api_hash, except_ids=except_ids)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.api_id))
        
        b.write(String(self.api_hash))
        
        b.write(Vector(self.except_ids, Int))
        
        return b.getvalue()
