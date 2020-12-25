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


class Poll(TLObject):
    """Attributes:
        LAYER: ``112``

    Attributes:
        ID: ``0x86e18161``

    Parameters:
        id: ``int`` ``64-bit``
        question: ``str``
        answers: List of :obj:`PollAnswer <pyrogram.api.types.PollAnswer>`
        closed (optional): ``bool``
        public_voters (optional): ``bool``
        multiple_choice (optional): ``bool``
        quiz (optional): ``bool``
        close_period (optional): ``int`` ``32-bit``
        close_date (optional): ``int`` ``32-bit``
    """

    __slots__ = ["id", "question", "answers", "closed", "public_voters", "multiple_choice", "quiz", "close_period", "close_date"]

    ID = 0x86e18161
    QUALNAME = "types.Poll"

    def __init__(self, *, id: int, question: str, answers: list, closed: bool = None, public_voters: bool = None, multiple_choice: bool = None, quiz: bool = None, close_period: int = None, close_date: int = None):
        self.id = id  # long
        self.closed = closed  # flags.0?true
        self.public_voters = public_voters  # flags.1?true
        self.multiple_choice = multiple_choice  # flags.2?true
        self.quiz = quiz  # flags.3?true
        self.question = question  # string
        self.answers = answers  # Vector<PollAnswer>
        self.close_period = close_period  # flags.4?int
        self.close_date = close_date  # flags.5?int

    @staticmethod
    def read(b: BytesIO, *args) -> "Poll":
        
        id = Long.read(b)
        flags = Int.read(b)
        
        closed = True if flags & (1 << 0) else False
        public_voters = True if flags & (1 << 1) else False
        multiple_choice = True if flags & (1 << 2) else False
        quiz = True if flags & (1 << 3) else False
        question = String.read(b)
        
        answers = TLObject.read(b)
        
        close_period = Int.read(b) if flags & (1 << 4) else None
        close_date = Int.read(b) if flags & (1 << 5) else None
        return Poll(id=id, question=question, answers=answers, closed=closed, public_voters=public_voters, multiple_choice=multiple_choice, quiz=quiz, close_period=close_period, close_date=close_date)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        flags = 0
        flags |= (1 << 0) if self.closed is not None else 0
        flags |= (1 << 1) if self.public_voters is not None else 0
        flags |= (1 << 2) if self.multiple_choice is not None else 0
        flags |= (1 << 3) if self.quiz is not None else 0
        flags |= (1 << 4) if self.close_period is not None else 0
        flags |= (1 << 5) if self.close_date is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.question))
        
        b.write(Vector(self.answers))
        
        if self.close_period is not None:
            b.write(Int(self.close_period))
        
        if self.close_date is not None:
            b.write(Int(self.close_date))
        
        return b.getvalue()
