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


class AcceptLoginToken(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0xe894ad4d``

    Parameters:
        token: ``bytes``

    Returns:
        :obj:`Authorization <pyrogram.api.types.Authorization>`
    """

    __slots__ = ["token"]

    ID = 0xe894ad4d
    QUALNAME = "functions.auth.AcceptLoginToken"

    def __init__(self, *, token: bytes):
        self.token = token  # bytes

    @staticmethod
    def read(b: BytesIO, *args) -> "AcceptLoginToken":
        # No flags
        
        token = Bytes.read(b)
        
        return AcceptLoginToken(token=token)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.token))
        
        return b.getvalue()
