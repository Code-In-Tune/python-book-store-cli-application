from dataclasses import dataclass
from decimal import Decimal

from bookstore.model.book.enums.availability import Availability


@dataclass
class BookRecord:
    book_id      : int
    title        : str
    author       : str
    isbn         : str
    publisher    : str
    price        : Decimal
    availability : Availability
    quantity     : int
