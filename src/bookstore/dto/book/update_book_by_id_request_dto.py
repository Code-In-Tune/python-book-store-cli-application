import dataclasses


@dataclasses.dataclass(frozen=True)
class UpdateBookByIdRequestDTO:
    book_id   : str
    title     : str
    author    : str
    isbn      : str
    publisher : str
    quantity  : str
    price     : str