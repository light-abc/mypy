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


class VotesList(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0x0823f649``

    Parameters:
        count: ``int`` ``32-bit``
        votes: List of either :obj:`MessageUserVote <pyrogram.api.types.MessageUserVote>`, :obj:`MessageUserVoteInputOption <pyrogram.api.types.MessageUserVoteInputOption>` or :obj:`MessageUserVoteMultiple <pyrogram.api.types.MessageUserVoteMultiple>`
        users: List of either :obj:`UserEmpty <pyrogram.api.types.UserEmpty>` or :obj:`User <pyrogram.api.types.User>`
        next_offset (optional): ``str``

    See Also:
        This object can be returned by :obj:`messages.GetPollVotes <pyrogram.api.functions.messages.GetPollVotes>`.
    """

    __slots__ = ["count", "votes", "users", "next_offset"]

    ID = 0x0823f649
    QUALNAME = "types.messages.VotesList"

    def __init__(self, *, count: int, votes: list, users: list, next_offset: str = None):
        self.count = count  # int
        self.votes = votes  # Vector<MessageUserVote>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args) -> "VotesList":
        flags = Int.read(b)
        
        count = Int.read(b)
        
        votes = TLObject.read(b)
        
        users = TLObject.read(b)
        
        next_offset = String.read(b) if flags & (1 << 0) else None
        return VotesList(count=count, votes=votes, users=users, next_offset=next_offset)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.votes))
        
        b.write(Vector(self.users))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        return b.getvalue()
