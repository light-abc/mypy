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


class UpdateDialogFiltersOrder(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0xc563c1e4``

    Parameters:
        order: List of ``int`` ``32-bit``

    Returns:
        ``bool``
    """

    __slots__ = ["order"]

    ID = 0xc563c1e4
    QUALNAME = "functions.messages.UpdateDialogFiltersOrder"

    def __init__(self, *, order: list):
        self.order = order  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdateDialogFiltersOrder":
        # No flags
        
        order = TLObject.read(b, Int)
        
        return UpdateDialogFiltersOrder(order=order)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.order, Int))
        
        return b.getvalue()
