import dataclasses


@dataclasses.dataclass(frozen=True)
class GetBookResponseDto:
    book_id      : str
    title        : str
    author       : str
    isbn         : str
    publisher    : str
    quantity     : str
    price        : str
    availability : str