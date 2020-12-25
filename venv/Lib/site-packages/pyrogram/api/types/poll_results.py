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


class PollResults(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0xbadcc1a3``

    Parameters:
        min (optional): ``bool``
        results (optional): List of :obj:`PollAnswerVoters <pyrogram.api.types.PollAnswerVoters>`
        total_voters (optional): ``int`` ``32-bit``
        recent_voters (optional): List of ``int`` ``32-bit``
        solution (optional): ``str``
        solution_entities (optional): List of either :obj:`MessageEntityUnknown <pyrogram.api.types.MessageEntityUnknown>`, :obj:`MessageEntityMention <pyrogram.api.types.MessageEntityMention>`, :obj:`MessageEntityHashtag <pyrogram.api.types.MessageEntityHashtag>`, :obj:`MessageEntityBotCommand <pyrogram.api.types.MessageEntityBotCommand>`, :obj:`MessageEntityUrl <pyrogram.api.types.MessageEntityUrl>`, :obj:`MessageEntityEmail <pyrogram.api.types.MessageEntityEmail>`, :obj:`MessageEntityBold <pyrogram.api.types.MessageEntityBold>`, :obj:`MessageEntityItalic <pyrogram.api.types.MessageEntityItalic>`, :obj:`MessageEntityCode <pyrogram.api.types.MessageEntityCode>`, :obj:`MessageEntityPre <pyrogram.api.types.MessageEntityPre>`, :obj:`MessageEntityTextUrl <pyrogram.api.types.MessageEntityTextUrl>`, :obj:`MessageEntityMentionName <pyrogram.api.types.MessageEntityMentionName>`, :obj:`InputMessageEntityMentionName <pyrogram.api.types.InputMessageEntityMentionName>`, :obj:`MessageEntityPhone <pyrogram.api.types.MessageEntityPhone>`, :obj:`MessageEntityCashtag <pyrogram.api.types.MessageEntityCashtag>`, :obj:`MessageEntityUnderline <pyrogram.api.types.MessageEntityUnderline>`, :obj:`MessageEntityStrike <pyrogram.api.types.MessageEntityStrike>`, :obj:`MessageEntityBlockquote <pyrogram.api.types.MessageEntityBlockquote>` or :obj:`MessageEntityBankCard <pyrogram.api.types.MessageEntityBankCard>`
    """

    __slots__ = ["min", "results", "total_voters", "recent_voters", "solution", "solution_entities"]

    ID = 0xbadcc1a3
    QUALNAME = "types.PollResults"

    def __init__(self, *, min: bool = None, results: list = None, total_voters: int = None, recent_voters: list = None, solution: str = None, solution_entities: list = None):
        self.min = min  # flags.0?true
        self.results = results  # flags.1?Vector<PollAnswerVoters>
        self.total_voters = total_voters  # flags.2?int
        self.recent_voters = recent_voters  # flags.3?Vector<int>
        self.solution = solution  # flags.4?string
        self.solution_entities = solution_entities  # flags.4?Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args) -> "PollResults":
        flags = Int.read(b)
        
        min = True if flags & (1 << 0) else False
        results = TLObject.read(b) if flags & (1 << 1) else []
        
        total_voters = Int.read(b) if flags & (1 << 2) else None
        recent_voters = TLObject.read(b, Int) if flags & (1 << 3) else []
        
        solution = String.read(b) if flags & (1 << 4) else None
        solution_entities = TLObject.read(b) if flags & (1 << 4) else []
        
        return PollResults(min=min, results=results, total_voters=total_voters, recent_voters=recent_voters, solution=solution, solution_entities=solution_entities)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.min is not None else 0
        flags |= (1 << 1) if self.results is not None else 0
        flags |= (1 << 2) if self.total_voters is not None else 0
        flags |= (1 << 3) if self.recent_voters is not None else 0
        flags |= (1 << 4) if self.solution is not None else 0
        flags |= (1 << 4) if self.solution_entities is not None else 0
        b.write(Int(flags))
        
        if self.results is not None:
            b.write(Vector(self.results))
        
        if self.total_voters is not None:
            b.write(Int(self.total_voters))
        
        if self.recent_voters is not None:
            b.write(Vector(self.recent_voters, Int))
        
        if self.solution is not None:
            b.write(String(self.solution))
        
        if self.solution_entities is not None:
            b.write(Vector(self.solution_entities))
        
        return b.getvalue()
