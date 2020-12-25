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


class SetContentSettings(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0xb574b16b``

    Parameters:
        sensitive_enabled (optional): ``bool``

    Returns:
        ``bool``
    """

    __slots__ = ["sensitive_enabled"]

    ID = 0xb574b16b
    QUALNAME = "functions.account.SetContentSettings"

    def __init__(self, *, sensitive_enabled: bool = None):
        self.sensitive_enabled = sensitive_enabled  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args) -> "SetContentSettings":
        flags = Int.read(b)
        
        sensitive_enabled = True if flags & (1 << 0) else False
        return SetContentSettings(sensitive_enabled=sensitive_enabled)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.sensitive_enabled is not None else 0
        b.write(Int(flags))
        
        return b.getvalue()
