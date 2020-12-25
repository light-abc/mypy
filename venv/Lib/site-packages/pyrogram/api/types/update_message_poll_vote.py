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


class UpdateMessagePollVote(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0x42f88f2c``

    Parameters:
        poll_id: ``int`` ``64-bit``
        user_id: ``int`` ``32-bit``
        options: List of ``bytes``
    """

    __slots__ = ["poll_id", "user_id", "options"]

    ID = 0x42f88f2c
    QUALNAME = "types.UpdateMessagePollVote"

    def __init__(self, *, poll_id: int, user_id: int, options: list):
        self.poll_id = poll_id  # long
        self.user_id = user_id  # int
        self.options = options  # Vector<bytes>

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdateMessagePollVote":
        # No flags
        
        poll_id = Long.read(b)
        
        user_id = Int.read(b)
        
        options = TLObject.read(b, Bytes)
        
        return UpdateMessagePollVote(poll_id=poll_id, user_id=user_id, options=options)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.poll_id))
        
        b.write(Int(self.user_id))
        
        b.write(Vector(self.options, Bytes))
        
        return b.getvalue()
