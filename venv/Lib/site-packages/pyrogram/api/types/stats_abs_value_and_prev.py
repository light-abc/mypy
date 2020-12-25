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


class StatsAbsValueAndPrev(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0xcb43acde``

    Parameters:
        current: ``float`` ``64-bit``
        previous: ``float`` ``64-bit``
    """

    __slots__ = ["current", "previous"]

    ID = 0xcb43acde
    QUALNAME = "types.StatsAbsValueAndPrev"

    def __init__(self, *, current: float, previous: float):
        self.current = current  # double
        self.previous = previous  # double

    @staticmethod
    def read(b: BytesIO, *args) -> "StatsAbsValueAndPrev":
        # No flags
        
        current = Double.read(b)
        
        previous = Double.read(b)
        
        return StatsAbsValueAndPrev(current=current, previous=previous)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Double(self.current))
        
        b.write(Double(self.previous))
        
        return b.getvalue()
