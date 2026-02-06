from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from bookstore.model.book.enums.availability import Availability


@dataclass
class BookRecord:
    title        : str
    author       : str
    isbn         : str
    publisher    : str
    price        : Decimal
    availability : Availability
    quantity     : int
    book_id      : Optional[int] = None
