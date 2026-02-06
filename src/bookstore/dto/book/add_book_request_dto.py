import dataclasses


@dataclasses.dataclass(frozen=True)
class AddBookRequestDTO:
    title     : str
    author    : str
    isbn      : str
    publisher : str
    quantity  : str
    price     : str