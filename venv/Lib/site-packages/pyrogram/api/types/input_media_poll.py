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


class InputMediaPoll(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0x0f94e5f1``

    Parameters:
        poll: :obj:`Poll <pyrogram.api.types.Poll>`
        correct_answers (optional): List of ``bytes``
        solution (optional): ``str``
        solution_entities (optional): List of either :obj:`MessageEntityUnknown <pyrogram.api.types.MessageEntityUnknown>`, :obj:`MessageEntityMention <pyrogram.api.types.MessageEntityMention>`, :obj:`MessageEntityHashtag <pyrogram.api.types.MessageEntityHashtag>`, :obj:`MessageEntityBotCommand <pyrogram.api.types.MessageEntityBotCommand>`, :obj:`MessageEntityUrl <pyrogram.api.types.MessageEntityUrl>`, :obj:`MessageEntityEmail <pyrogram.api.types.MessageEntityEmail>`, :obj:`MessageEntityBold <pyrogram.api.types.MessageEntityBold>`, :obj:`MessageEntityItalic <pyrogram.api.types.MessageEntityItalic>`, :obj:`MessageEntityCode <pyrogram.api.types.MessageEntityCode>`, :obj:`MessageEntityPre <pyrogram.api.types.MessageEntityPre>`, :obj:`MessageEntityTextUrl <pyrogram.api.types.MessageEntityTextUrl>`, :obj:`MessageEntityMentionName <pyrogram.api.types.MessageEntityMentionName>`, :obj:`InputMessageEntityMentionName <pyrogram.api.types.InputMessageEntityMentionName>`, :obj:`MessageEntityPhone <pyrogram.api.types.MessageEntityPhone>`, :obj:`MessageEntityCashtag <pyrogram.api.types.MessageEntityCashtag>`, :obj:`MessageEntityUnderline <pyrogram.api.types.MessageEntityUnderline>`, :obj:`MessageEntityStrike <pyrogram.api.types.MessageEntityStrike>`, :obj:`MessageEntityBlockquote <pyrogram.api.types.MessageEntityBlockquote>` or :obj:`MessageEntityBankCard <pyrogram.api.types.MessageEntityBankCard>`
    """

    __slots__ = ["poll", "correct_answers", "solution", "solution_entities"]

    ID = 0x0f94e5f1
    QUALNAME = "types.InputMediaPoll"

    def __init__(self, *, poll, correct_answers: list = None, solution: str = None, solution_entities: list = None):
        self.poll = poll  # Poll
        self.correct_answers = correct_answers  # flags.0?Vector<bytes>
        self.solution = solution  # flags.1?string
        self.solution_entities = solution_entities  # flags.1?Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args) -> "InputMediaPoll":
        flags = Int.read(b)
        
        poll = TLObject.read(b)
        
        correct_answers = TLObject.read(b, Bytes) if flags & (1 << 0) else []
        
        solution = String.read(b) if flags & (1 << 1) else None
        solution_entities = TLObject.read(b) if flags & (1 << 1) else []
        
        return InputMediaPoll(poll=poll, correct_answers=correct_answers, solution=solution, solution_entities=solution_entities)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.correct_answers is not None else 0
        flags |= (1 << 1) if self.solution is not None else 0
        flags |= (1 << 1) if self.solution_entities is not None else 0
        b.write(Int(flags))
        
        b.write(self.poll.write())
        
        if self.correct_answers is not None:
            b.write(Vector(self.correct_answers, Bytes))
        
        if self.solution is not None:
            b.write(String(self.solution))
        
        if self.solution_entities is not None:
            b.write(Vector(self.solution_entities))
        
        return b.getvalue()
