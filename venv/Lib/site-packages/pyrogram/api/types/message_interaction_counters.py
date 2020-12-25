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


class MessageInteractionCounters(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0xad4fc9bd``

    Parameters:
        msg_id: ``int`` ``32-bit``
        views: ``int`` ``32-bit``
        forwards: ``int`` ``32-bit``
    """

    __slots__ = ["msg_id", "views", "forwards"]

    ID = 0xad4fc9bd
    QUALNAME = "types.MessageInteractionCounters"

    def __init__(self, *, msg_id: int, views: int, forwards: int):
        self.msg_id = msg_id  # int
        self.views = views  # int
        self.forwards = forwards  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "MessageInteractionCounters":
        # No flags
        
        msg_id = Int.read(b)
        
        views = Int.read(b)
        
        forwards = Int.read(b)
        
        return MessageInteractionCounters(msg_id=msg_id, views=views, forwards=forwards)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.msg_id))
        
        b.write(Int(self.views))
        
        b.write(Int(self.forwards))
        
        return b.getvalue()
